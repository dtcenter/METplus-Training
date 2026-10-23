"""Check repaired emphasis against the original review and Drupal snapshot.

Run from the repository root:
  python inventory/validate_emphasis.py --html /tmp/metplus-emphasis-html \
    --source /tmp/metplus-v5-drupal.html
Requires beautifulsoup4. Does not fetch remote resources.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata

from bs4 import BeautifulSoup


def normalized(text):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', text).lower())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    inventory = Path(__file__).resolve().parent
    repo = inventory.parent
    audit = json.loads((inventory / 'published-rtd-validation.json').read_text())
    source = BeautifulSoup(args.source.read_text(), 'html.parser')
    source_strong = {normalized(t.get_text()) for t in source.select('strong,b')}
    checked = spans = 0
    errors = []
    for page in audit['pages']:
        html = BeautifulSoup((args.html / 'Tutorial/v5.0' / page['page']).read_text(),
                             'html.parser')
        body = html.select_one('[role=main]')
        paragraphs = [p for p in body.select('p,li') if not p.select('pre')
                      and (p.name == 'p' or not p.select('p'))]
        leftovers = [p.get_text() for p in paragraphs if '**' in p.get_text()]
        if leftovers:
            errors.append(f"{page['page']}: {len(leftovers)} prose elements expose **")
        rst = (repo / 'docs/Tutorial/v5.0' / page['page']).with_suffix('.rst')
        lines = rst.read_text().splitlines()
        for original in page['prose_with_literal_strong_markers']:
            key = normalized(original['text'])
            matches = [p for p in paragraphs if normalized(p.get_text()) == key
                       and p.find_parent('section').get('id') == original['section']]
            # A list item may wrap a matching paragraph; prefer the paragraph.
            matches = [p for p in matches if p.name == 'p'] or matches
            def rst_text(line):
                return re.sub(r'(?:<[^>]+>|:ref:)', '', line)
            rst_matches = [line for line in lines if '**' in line
                           and normalized(rst_text(line)) == key]
            # Repeated source prose can occur in multiple sections.
            rst_matches = list(dict.fromkeys(rst_matches))
            if len(matches) != 1 or len(rst_matches) != 1:
                errors.append(f"{page['page']}: repaired paragraph not unique: {key[:60]}")
                continue
            expected = [normalized(t) for t in re.findall(r'\*\*(.*?)\*\*', rst_matches[0])]
            actual = [normalized(t.get_text()) for t in matches[0].select('strong')]
            if Counter(expected) != Counter(actual):
                errors.append(f"{page['page']}: rendered bold spans differ: {expected} / {actual}")
            for span in expected:
                if span not in source_strong:
                    errors.append(f"{page['page']}: bold span absent from Drupal: {span}")
            checked += 1
            spans += len(expected)
    result = {'repaired_prose_elements_checked': checked,
              'bold_spans_checked': spans, 'errors': errors}
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(errors) or checked != 65)


if __name__ == '__main__':
    main()
