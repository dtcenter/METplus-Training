"""Audit links in the published v5.0 practical without modifying destinations.

Requires requests and beautifulsoup4. Reports HTTP access and HTML fragment
presence; does not execute exercises or download entire binary data files.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.parse import urljoin, urldefrag, unquote, urlsplit, urlunsplit

from bs4 import BeautifulSoup
import requests

BASE = 'https://metplus.readthedocs.io/projects/metplus-training/en/feature_69_drupal2rtd_auto/'


def request(url):
    result = {'requested_url': url}
    try:
        with requests.get(url, stream=True, timeout=(12, 30)) as response:
            result.update(status=response.status_code, final_url=response.url,
                          content_type=response.headers.get('Content-Type', ''),
                          redirects=[r.url for r in response.history])
            if response.ok and 'html' in result['content_type'].lower():
                chunks, size = [], 0
                for chunk in response.iter_content(65536):
                    chunks.append(chunk)
                    size += len(chunk)
                    if size > 8 * 1024 * 1024:
                        result['html_truncated'] = True
                        break
                result['_html'] = b''.join(chunks)
    except requests.RequestException as error:
        result['error'] = str(error)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default=BASE)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--cache', type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    names = ['index.html', 'Basic_Verification_Statistics_Review.html',
             'Preliminary_work_METplus_setup.html']
    names += [next((repo / 'docs/Tutorial/v5.0').glob(f'Session_{n}_*.rst')).with_suffix('.html').name
              for n in range(1, 12)] + ['Tutorial_Survey.html']
    args.cache.mkdir(exist_ok=True, parents=True)
    pages = [urljoin(args.base, 'Tutorial/v5.0/'+name) for name in names]
    fetched, links, page_errors = {}, {}, []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, result in zip(pages, pool.map(request, pages)):
            fetched[url] = result
            if result.get('status') != 200 or '_html' not in result:
                page_errors.append({k: v for k, v in result.items() if not k.startswith('_')})
                continue
            (args.cache / url.split('/')[-1]).write_bytes(result['_html'])
            soup = BeautifulSoup(result['_html'], 'html.parser')
            body = soup.select_one('[role=main]')
            for anchor in body.select('a[href]'):
                href = anchor['href']
                if not href or href.startswith(('mailto:', 'javascript:')):
                    continue
                target = urljoin(url, href)
                if urlsplit(target).scheme not in ['http', 'https', 'ftp']:
                    continue
                links.setdefault(target, []).append({'page': url.split('/')[-1],
                                                      'label': anchor.get_text(' ', strip=True)})
    destinations = {urldefrag(url)[0] for url in links}
    pending = sorted(destinations - fetched.keys())
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, result in zip(pending, pool.map(request, pending)):
            fetched[url] = result
    # An HTTPS retry is evidence only; the original URL is still reported.
    retry_urls = {}
    for url, result in fetched.items():
        if url.startswith('http:') and (result.get('status', 0) >= 400 or 'error' in result):
            parts = urlsplit(url)
            retry_urls[url] = urlunsplit(('https', parts.netloc, parts.path, parts.query, ''))
    with ThreadPoolExecutor(max_workers=6) as pool:
        retries = dict(zip(retry_urls, pool.map(request, retry_urls.values())))
    documents = {}
    results = []
    for url, occurrences in sorted(links.items()):
        dest, fragment = urldefrag(url)
        raw = fetched[dest]
        row = {k: v for k, v in raw.items() if not k.startswith('_')}
        row.update(url=url, occurrences=occurrences,
                   internal=dest.startswith(args.base), fragment=unquote(fragment))
        if fragment and '_html' in raw:
            if dest not in documents:
                doc = BeautifulSoup(raw['_html'], 'html.parser')
                documents[dest] = {t.get('id') for t in doc.select('[id]')} | {t.get('name') for t in doc.select('a[name]')}
            row['fragment_present'] = unquote(fragment) in documents[dest]
        elif fragment:
            row['fragment_present'] = None
        if dest in retries:
            row['https_retry'] = {k: v for k, v in retries[dest].items() if not k.startswith('_')}
        if '_html' in raw:
            doc = BeautifulSoup(raw['_html'], 'html.parser')
            row['destination_title'] = doc.title.get_text(' ', strip=True) if doc.title else ''
        results.append(row)
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'base': args.base,
              'pages_checked': len(pages), 'link_occurrences': sum(map(len, links.values())),
              'unique_link_targets': len(links), 'unique_fetch_urls': len(destinations),
              'page_errors': page_errors, 'results': results}
    args.report.write_text(json.dumps(report, indent=2)+'\n')
    issues = [r for r in results if r.get('status') != 200 or r.get('error') or r.get('fragment_present') is False]
    print(json.dumps({k: v for k, v in report.items() if k != 'results'}, indent=2))
    print(json.dumps({'issues': issues}, indent=2))


if __name__ == '__main__':
    main()
