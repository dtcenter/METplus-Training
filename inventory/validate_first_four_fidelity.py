"""Compare the first four v5.0 chapters with a supplied historical Drupal export.

Requires beautifulsoup4. See first-four-fidelity-report.md for scope and explicit
native image representations and presentation adaptations.
"""
import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote, parse_qsl, urlencode
from bs4 import BeautifulSoup
from validate_conversion import plain, compact, headings

NAMES = [('Basic_Verification_Statistics_Review', '/basic-verification-statistics-review'),
         ('Preliminary_work_METplus_setup', '/preliminary-work-metplus-setup'),
         ('Session_1_Grid-to-Grid', '/session-1-grid-grid'),
         ('Session_2_Grid-to-Obs', '/session-2-grid-obs')]
INVENTORY = Path(__file__).resolve().parent
REPO = INVENTORY.parent
POLICY = json.loads((INVENTORY / 'first-four-link-policy.json').read_text())


def target(url, name):
    if url.startswith('/'):
        url = urljoin('https://dtcenter.org', url)
    url = url.replace('http://met.readthedocs.io/', 'https://met.readthedocs.io/')
    if not url.startswith(('http:', 'https:', 'ftp:')):
        return urljoin('https://local.invalid/'+name+'.html', url).split('https://local.invalid/')[-1]
    url = urljoin('https://dtcenter.org', url)
    parts = urlsplit(url)
    if parts.netloc in ['dtcenter.org', 'www.dtcenter.org']:
        for suffix, dest in sorted(POLICY['local_suffixes'].items(), key=lambda x: -len(x[0])):
            if parts.path.rstrip('/').endswith(suffix):
                return dest
    url = url.replace('https://www.github.com/', 'https://github.com/')
    url = url.replace('https://met.readthedocs.io/en/', 'https://metplus.readthedocs.io/projects/met/en/')
    url = url.replace('/projects/met/en/latest/', '/projects/met/en/main_v11.1/')
    for project, version in [('metplus', '5.1'), ('metviewer', '5.1'), ('metplotpy', '2.1'), ('metdataio', '2.1')]:
        url = url.replace(f'https://{project}.readthedocs.io/en/latest/', f'https://{project}.readthedocs.io/en/main_v{version}/')
    url = url.replace('/en/main_v4.0/', '/en/main_v5.1/')
    url = url.replace('/met/data/config/', '/data/config/')
    if '/projects/met/' in url or 'github.com/dtcenter/MET/blob/' in url:
        url = re.sub(r'/main_v(?:10\.0|11\.0|11\.1)/', '/main_v11.x/', url)
    url = POLICY['external_aliases'].get(url.rstrip('/'), url)
    parts = urlsplit(url)
    query = urlencode([(k, v) for k, v in parse_qsl(parts.query) if k != 'highlight'])
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip('/'), query, parts.fragment))


def normalized(text):
    return re.sub('[^a-z0-9]', '', text.lower())


def prose_text(node, name, raw_targets):
    node = copy.deepcopy(node)
    for a in node.select('a[href]'):
        key = target(a['href'], name)
        if key in raw_targets:
            a.clear()
            a.append('LINK'+key)
    text = node.get_text(' ', strip=True)
    text = re.sub(r'^(?:IMPORTANT NOTE|NOTE|Note):\s*', '', text)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('--baseline', default='83517df')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    source = BeautifulSoup(args.source.read_text(), 'html.parser')
    representations = json.loads((INVENTORY / 'first-four-native-representations.json').read_text())
    errors, rows = [], []
    for name, prefix in NAMES:
        articles = [a for a in source.select('article.node') if prefix in a.find('h2').a['href']]
        rst = Path('docs/Tutorial/v5.0') / (name+'.rst')
        htmlfile = args.html / 'Tutorial/v5.0' / (name+'.html')
        body = BeautifulSoup(htmlfile.read_text(), 'html.parser').select_one('[role=main]')
        for t in body.select('.admonition-title'):
            t.decompose()
        pre = [compact(p.get_text()) for p in body.select('pre')]
        source_blocks = [b for a in articles for b in a.select('.codeblock,.greyblock')]
        missing_literals = []
        legend_adaptations = 0
        ordered_stream = '\n'.join(pre)
        cursor = 0
        for b in source_blocks:
            text = compact(plain(b))
            # The overview's color key was adapted to Sphinx's existing theme.
            if text == compact('Text in GRAY boxes are sample output from a command or contents of a file.'):
                legend_adaptations += 1
                continue
            position = ordered_stream.find(text, cursor)
            if position < 0:
                missing_literals.append(plain(b))
            else:
                cursor = position + len(text)
        # Reverse coverage catches extra characters such as an appended zero.
        original_plain = compact(''.join(plain(a.select_one('.node__content')) for a in articles))
        extra_literals = [b for b in pre if b not in original_plain]
        expected = Counter(target(a['href'], name) for article in articles for a in article.select('.node__content a[href]'))
        actual = Counter(target(a['href'], name) for a in body.select('a.reference[href]'))
        missing_links = dict(expected-actual)
        raw_targets = {target(a['href'], name) for article in articles for a in article.select('.node__content a[href]') if a.get_text(' ', strip=True).startswith(('http:', 'https:'))}
        missing_prose, count = [], 0
        text = normalized(prose_text(body, name, raw_targets))
        for article in articles:
            for p in article.select('.node__content p,.node__content li,.blueblock,.redblock,.yellowblock,.greenblock'):
                original = prose_text(p, name, raw_targets)
                if len(original) < 20:
                    continue
                count += 1
                if name == 'Session_1_Grid-to-Grid':
                    original = original.replace('code blocks in BOLD white text with a black background', 'code blocks have green text with a white background')
                    original = original.replace('Text in YELLOW boxes', 'Text in GREEN boxes').replace('Text in BLUE boxes', 'Text in ORANGE boxes')
                if normalized(original) not in text:
                    missing_prose.append(p.get_text(' ', strip=True))
        source_images = Counter(unquote(i['src'].split('/')[-1]) for a in articles for i in a.select('.node__content img'))
        images = body.select('img')
        actual_images = Counter(unquote(i['src'].split('/')[-1]) for i in images)
        represented = Counter()
        native_errors = []
        if name == NAMES[0][0]:
            equations = [m.get_text().strip() for m in body.select('div.math')]
            tables = [[[c.get_text(' ', strip=True) for c in row.select('th,td')] for row in table.select('tr')] for table in body.select('table')]
            for item in representations:
                value = item['latex'] if item['type']=='math' else item['cells']
                available = equations if item['type']=='math' else tables
                if value not in available:
                    native_errors.append(item['source_image'])
                represented[item['source_image']] += 1
        figure_errors = []
        for im in images:
            if not (htmlfile.parent / unquote(im['src'])).resolve().is_file() or not im.get('alt', '').strip():
                figure_errors.append(im['src'])
        missing_images = dict(source_images-actual_images-represented)
        usage_errors = []
        usage_fixture = json.loads((INVENTORY / 'first-four-usage-tables.json').read_text())
        usage_count = 0
        for item in usage_fixture:
            if item['chapter'] != name:
                continue
            usage_count += 1
            table = next((t for t in body.select('table') if item['caption'] in t.get_text(' ', strip=True)), None)
            def cell(text):
                return compact(text).replace('…', '...').translate(str.maketrans({'“': chr(34), '”': chr(34), '’': chr(39)}))
            actual_cells = [[cell(c.get_text(' ', strip=True)) for c in row.select('th,td')] for row in table.select('tr')] if table else []
            expected_cells = [[cell(c) for c in row] for row in item['cells']]
            if actual_cells != expected_cells:
                usage_errors.append(item['caption'])
        old = subprocess.check_output(['git','show',f'{args.baseline}:{rst}'], cwd=REPO, text=True)
        new_rst = (REPO / rst).read_text()
        same_headings = headings(old) == headings(new_rst)
        old_labels = set(re.findall(r'^\.\. _([^:]+):', old, flags=re.M))
        new_labels = set(re.findall(r'^\.\. _([^:]+):', new_rst, flags=re.M))
        labels_preserved = old_labels <= new_labels
        internal_link_errors = []
        for link in body.select('a.reference.internal[href]'):
            path, _, fragment = link['href'].partition('#')
            destination = htmlfile.parent / path if path else htmlfile
            if not destination.is_file() or (fragment and BeautifulSoup(destination.read_text(), 'html.parser').find(id=unquote(fragment)) is None):
                internal_link_errors.append(link['href'])
        row = dict(chapter=name, source_pages=len(articles), source_literal_blocks=len(source_blocks),
                   literal_blocks_checked=len(source_blocks)-legend_adaptations, legend_blocks_adapted=legend_adaptations,
                   rendered_literal_blocks=len(pre), missing_literals=missing_literals, extra_literals=extra_literals,
                   source_link_occurrences=sum(expected.values()), missing_links=missing_links,
                   prose_callout_units_checked=count, missing_prose=missing_prose,
                   source_image_occurrences=sum(source_images.values()), rendered_images=len(images),
                   native_image_representations=sum(represented.values()), missing_images=missing_images,
                   native_representation_errors=native_errors, figure_errors=figure_errors, source_usage_tables=usage_count, usage_table_errors=usage_errors, headings_preserved=same_headings, explicit_labels_preserved=labels_preserved, internal_link_errors=internal_link_errors)
        rows.append(row)
        if any([missing_literals, extra_literals, missing_links, missing_prose, missing_images, native_errors, figure_errors, usage_errors, not same_headings, not labels_preserved, internal_link_errors]):
            errors.append(name)
    diagnostics = [l for l in args.log.read_text().splitlines() if re.search(r'\b(?:WARNING|ERROR|CRITICAL):', l)]
    if diagnostics:
        errors.extend(diagnostics)
    result = dict(source_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest(), chapters=rows, errors=errors)
    args.report.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
