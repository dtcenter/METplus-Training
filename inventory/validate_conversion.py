"""Validate conversion fidelity against a downloaded Drupal full-book export.

Requires beautifulsoup4. Build the docs first, then run:
  python3 inventory/validate_conversion.py --source /tmp/metplus-v5-drupal.html \
      --html /tmp/metplus-pinned-html --log /tmp/metplus-pinned-build.log
The source snapshot is intentionally supplied explicitly, not fetched implicitly.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urljoin

from bs4 import BeautifulSoup, NavigableString


def plain(node):
    if isinstance(node, NavigableString):
        return str(node)
    return ('\n' if node.name == 'br' else '') + ''.join(plain(c) for c in node.children)


def compact(text):
    return re.sub(r'\s+', '', text.replace('\xa0', ' '))


def headings(text):
    lines = text.splitlines()
    return [lines[i-1].strip() for i in range(1, len(lines))
            if re.fullmatch(r'[=\-^"~]{3,}', lines[i]) and lines[i-1].strip()]


def canonical(url):
    url = urljoin('https://dtcenter.org', url)
    url = url.replace('https://met.readthedocs.io/en/latest/',
                      'https://metplus.readthedocs.io/projects/met/en/main_v11.1/')
    for project, version in [('metplus', '5.1'), ('metviewer', '5.1'),
                             ('metplotpy', '2.1'), ('metdataio', '2.1')]:
        url = url.replace(f'https://{project}.readthedocs.io/en/latest/',
                          f'https://{project}.readthedocs.io/en/main_v{version}/')
    url = url.replace('/main_v11.0/', '/main_v11.1/')
    url = url.replace('/met/data/config/', '/data/config/')
    if 'MET_Users_Guide_v9.0.latest.pdf' in url:
        url = 'https://metplus.readthedocs.io/projects/met/en/main_v11.1/Users_Guide/mode.html'
    if url.endswith('Users_Guide'):
        url += '/index.html'
    if url == 'ftp://ftp.nhc.noaa.gov/atcf/archive':
        url = 'https://ftp.nhc.noaa.gov/atcf/archive/'
    return url


def internal(url):
    if 'verify-environment-set-correctly' in url:
        return 'Preliminary_work_METplus_setup.html#verif-env-set-correct'
    if 'setting-tutorial-environment-seneca' in url:
        return 'Preliminary_work_METplus_setup.html#set-tut-env-seneca'
    if 'metplus-initial-setup' in url:
        return 'Preliminary_work_METplus_setup.html#metplus-initial-setup'
    if '/session-8-metplus-analysis-tools/metdataio' in url:
        return 'Session_8_METplus_Analysis_Tools.html#metdataio'
    return canonical(url)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('--baseline', default='e116336')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    soup = BeautifulSoup(args.source.read_text(), 'html.parser')
    articles = soup.select('article.node')
    report, errors = [], []
    for n in list(range(3, 12)) + ['survey']:
        rst = (next(Path('docs/Tutorial/v5.0').glob(f'Session_{n}_*.rst'))
               if n != 'survey' else Path('docs/Tutorial/v5.0/Tutorial_Survey.rst'))
        pages = [a for a in articles if (f'/session-{n}-' in a.find('h2').a['href']
                 if n != 'survey' else a.find('h2').a['href'].endswith('/tutorial-survey'))]
        rendered = args.html / 'Tutorial/v5.0' / rst.with_suffix('.html').name
        doc = BeautifulSoup(rendered.read_text(), 'html.parser')
        body = doc.select_one('div[role=main]')
        source_blocks = [t for a in pages for t in a.select('.codeblock, .greyblock')]
        blocks = body.select('div.highlight pre')
        mismatch = [i for i, (a, b) in enumerate(zip(source_blocks, blocks))
                    if compact(plain(a)) != compact(b.get_text())]
        if len(source_blocks) != len(blocks) or mismatch:
            errors.append(f'{rst.name}: literal-block count or content mismatch: {mismatch}')
        source_images = [i for a in pages for i in a.select('.node__content img')]
        images = body.select('img')
        if len(source_images) != len(images):
            errors.append(f'{rst.name}: image count mismatch')
        source_names = Counter(unquote(i['src'].split('/')[-1]).replace(' ', '')
                               for i in source_images)
        actual_names = Counter(unquote(i['src'].split('/')[-1]).replace(' ', '')
                               for i in images)
        if source_names != actual_names:
            errors.append(f'{rst.name}: figure identities differ from source')
        for im in images:
            target = (rendered.parent / unquote(im['src'])).resolve()
            if not target.is_file() or not im.get('alt', '').strip():
                errors.append(f'{rst.name}: image missing or no alt text: {im}')
        for link in body.select('a.reference[href]'):
            if re.search(r'/(latest|develop|master|main)/', link['href']):
                errors.append(f"{rst.name}: moving target {link['href']}")
        expected = Counter(internal(a['href']) for p in pages
                           for a in p.select('.node__content a[href]'))
        actual = Counter(canonical(a['href']) if a['href'].startswith(('http', 'ftp'))
                         else a['href'] for a in body.select('a.reference[href]'))
        missing = expected - actual
        if missing:
            errors.append(f'{rst.name}: missing source link targets: {dict(missing)}')
        for target in actual:
            if target.startswith('mailto:'):
                continue
            if target.startswith(('http', 'ftp')):
                if re.search(r'/(latest|develop|master|main)/', target):
                    errors.append(f'{rst.name}: moving target {target}')
                continue
            path, _, fragment = target.partition('#')
            dest = rendered.parent / path if path else rendered
            if not dest.is_file():
                errors.append(f'{rst.name}: missing internal page {target}')
            elif fragment:
                target_doc = BeautifulSoup(dest.read_text(), 'html.parser')
                if target_doc.find(id=fragment) is None:
                    errors.append(f'{rst.name}: missing internal anchor {target}')
        # Check substantive prose independently of layout and callout titles.
        for title in body.select('.admonition-title'):
            title.decompose()
        prose = re.sub('[^a-z0-9]', '', body.get_text(' ', strip=True).lower())
        prose_count, prose_missing = 0, []
        for page in pages:
            for para in page.select('.node__content p, .node__content li'):
                original = para.get_text(' ', strip=True)
                if len(original) < 45:
                    continue
                prose_count += 1
                expected_text = re.sub(r'(?:https?|ftp)://[^\s<>]+',
                                       lambda m: canonical(m[0]), original)
                expected_text = expected_text.replace('Chapter 14', 'the MODE chapter')
                if n == 8:
                    expected_text = expected_text.replace('completed Session 5!', 'completed Session 8!')
                    expected_text = expected_text.replace('<folder_tmpl> </folder_tmpl>',
                                                          '<folder_tmpl> and </folder_tmpl>')
                normalized = re.sub('[^a-z0-9]', '', expected_text.lower())
                if normalized not in prose:
                    prose_missing.append(original)
        if prose_missing:
            errors.append(f'{rst.name}: prose not found: {prose_missing}')
        old = subprocess.check_output(['git', 'show', f'{args.baseline}:{rst}'], text=True)
        if headings(old) != headings(rst.read_text()):
            errors.append(f'{rst.name}: heading text/order changed')
        report.append(dict(chapter=n, source_pages=len(pages), literal_blocks=len(blocks),
                           figures=len(images), source_link_occurrences=sum(expected.values()),
                           literal_mismatches=mismatch, missing_link_targets=dict(missing),
                           prose_checked=prose_count, prose_missing=prose_missing))
    scoped = [l for l in args.log.read_text().splitlines()
              if re.search(r'(Session_(?:[3-9]|1[01])_|Tutorial_Survey)', l)
              and ('WARNING:' in l or 'ERROR:' in l)]
    errors += scoped
    result = dict(chapters=report, scoped_warnings=scoped, errors=errors)
    if args.report:
        args.report.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
