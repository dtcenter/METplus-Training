"""Validate the authorized diagnostic repairs without claiming a full source audit.

Run from the repository root with --html BUILD --log BUILD_LOG.
Requires beautifulsoup4. Baseline defaults to the pre-repair commit.
"""
import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re
import subprocess

from bs4 import BeautifulSoup

NAMES = ['Basic_Verification_Statistics_Review', 'Preliminary_work_METplus_setup',
         'Session_1_Grid-to-Grid', 'Session_2_Grid-to-Obs']


def canonical(text):
    # Decode the escaped HTML left by the original conversion. Remove only
    # conversion markup; preserve punctuation/operators and all substantive text.
    for _ in range(3):
        text = html.unescape(text)
    text = re.sub(r'\*\*<em>(.*?)</em>\*\*', r'**\1**', text)
    text = text.replace('<em>', '*').replace('</em>', '*')
    text = re.sub(r'</?p>|<br\s*/?>', '', text)
    text = re.sub(r'^\s*(?:\d+\. )?\.\. [^\n]*', '', text, flags=re.M)
    text = text.replace('3, Based on these observations', '3. Based on these observations')
    # Remove only strong delimiters, preserving literal asterisk runs.
    text = re.sub(r'(?<!\*)\*\*(?!\*)', '', text)
    text = re.sub(r'(?<=`)__(?!_)', '_', text)
    return re.sub(r'\s+', '', text)


def headings(text):
    lines = text.splitlines()
    return [lines[i-1].strip() for i in range(1, len(lines))
            if re.fullmatch(r'[=\-^"~]{3,}', lines[i].strip()) and lines[i-1].strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('--baseline', default='1947d82')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    errors, chapters = [], []
    for name in NAMES:
        rel = f'docs/Tutorial/v5.0/{name}.rst'
        old = subprocess.check_output(['git', 'show', f'{args.baseline}:{rel}'], cwd=repo, text=True)
        new = (repo / rel).read_text()
        preserved = canonical(old) == canonical(new)
        same_headings = headings(old) == headings(new)
        same_links = Counter(re.findall(r'https?://[^\s<>`]+', old)) == Counter(re.findall(r'https?://[^\s<>`]+', new))
        labels = set(re.findall(r'^\.\. _([^:]+):', old, flags=re.M))
        new_labels = set(re.findall(r'^\.\. _([^:]+):', new, flags=re.M))
        body_path = args.html / 'Tutorial/v5.0' / f'{name}.html'
        body = BeautifulSoup(body_path.read_text(), 'html.parser').select_one('[role=main]')
        internal_errors = []
        for link in body.select('a.reference.internal[href]'):
            dest, _, fragment = link['href'].partition('#')
            target = body_path.parent / dest if dest else body_path
            if not target.is_file() or (fragment and BeautifulSoup(target.read_text(), 'html.parser').find(id=fragment) is None):
                internal_errors.append(link['href'])
        literal_separators_preserved = Counter(re.findall(r'\*{4,}', old)) == Counter(re.findall(r'\*{4,}', new))
        rendered_separator_count = sum(len(re.findall(r'\*{4,}', p.get_text())) for p in body.select('pre'))
        expected_separator_count = len(re.findall(r'\*{4,}', old))
        prose_markers = [p.get_text() for p in body.select('p') if '**' in p.get_text()]
        checks = {'text_preserved_after_markup_recovery': preserved, 'headings_preserved': same_headings,
                  'external_urls_unchanged': same_links,
                  'literal_asterisk_separators_preserved': literal_separators_preserved,
                  'literal_asterisk_separators_rendered': rendered_separator_count == expected_separator_count, 'existing_explicit_labels_preserved': labels <= new_labels,
                  'rendered_system_messages': len(body.select('.system-message')),
                  'unresolved_internal_links': internal_errors, 'prose_with_literal_strong_markers': prose_markers}
        if not all([preserved, same_headings, same_links, labels <= new_labels,
                    literal_separators_preserved, rendered_separator_count == expected_separator_count]) or checks['rendered_system_messages'] or internal_errors or prose_markers:
            errors.append(name)
        chapters.append({'chapter': name, **checks})
    diagnostics = [line for line in args.log.read_text().splitlines()
                   if re.search(r'\b(?:WARNING|ERROR|CRITICAL):', line)]
    if diagnostics:
        errors.append('Build diagnostics remain')
    result = {'baseline': args.baseline, 'chapters': chapters, 'build_diagnostics': diagnostics, 'errors': errors}
    if args.report:
        args.report.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
