# Published responsive verification and fresh link audit

Reviewed 2026-10-23 local time (the machine-readable audit records its UTC timestamp). This fresh audit was authorized after commit `5218457`; the original outstanding-link list was never supplied. This report provides a current link baseline rather than reconstructing that missing list.

## Deployed responsive changes

The published stylesheet, all 14 chapter bodies, and the four earlier chapters' published source files match the validated `5218457` build. This includes the restored Preliminary Work sample-log separators. All 69 checked resource/navigation URLs load and their checked internal anchors resolve. See [deployment evidence](responsive-deployment-validation.json).

The live Firefox 158.0.1 review passes **153 page/width cases**: 14 published chapters and three index pages at 320, 390, 767, 768, 769, 1024, 1100, 1101, and 1280 pixels. No page-level overflow, broken images, or failed horizontal-scroll tests remain. MathJax's startup promise was awaited where available. Sampled screenshots confirm tables and literal blocks remain usable in their scroll containers; this is not a review of every screen position. See [published browser results](published-responsive-validation.json). Temporary screenshots are in `/tmp/metplus-published-responsive-browser`.

## Link results

The tutorial index and 14 chapters contain **728 checked link occurrences**, including heading permalinks: **399 unique targets**, comprising 255 internal targets and 144 external targets. They resolve through 102 distinct fetch URLs (15 internal and 87 external). All 315 checked HTML fragments exist: 241 internal and 74 external. No missing internal page or fragment was found.

The HTTP pass produced four exceptions; browser follow-up distinguishes request filtering from unavailable content. HTTP 200 alone also does not establish that a redirected page still provides the requested material.

| Destination | Chapter | Finding |
|---|---|---|
| Navy ATCF `abdeck.txt` | Session 6 | Original HTTP URL times out. HTTPS redirects to the general NRL Monterey location page, which Firefox can open, but the ATCF document is absent. This source destination remains unavailable. |
| GFDL Vortex Tracker download | Session 6 | HTTP 200 redirect to DTC's general legacy-tools notice; the requested download/documentation page is no longer supplied there. |
| NWP Containers tutorial | Session 8 | HTTP 200 redirect to the same DTC legacy-tools notice; the requested tutorial is no longer supplied there. |
| MET-Help archive | Survey | Automated GET returns 403, but Firefox opens the real archive index with monthly archive links. The earlier claim of inaccessibility is superseded for browser access. Individual monthly archive links were not recursively audited. |
| Natural Earth homepage and downloads | Session 1 | Automated GET returns 406 for both URLs, but Firefox opens their expected content with HTTP 200. These are request-filtering exceptions, not demonstrated broken links. |

DTC's [legacy-tools notice](https://dtcenter.org/community-code-legacy-tools) states that it stopped providing the affected documentation and tutorial materials in April 2024. No unverified mirrors or modern replacements were substituted. The Navy and two retired DTC destinations remain the three content-availability findings.

One older Seneca setup URL in Session 8 still goes through Drupal, but redirects to the correct historical Seneca page. Its corresponding Sphinx target exists (`Preliminary_work_METplus_setup.html#set-tut-env-seneca`); localizing this link is an optional conversion cleanup, not a broken-link fix. Other observed redirects include HTTP-to-HTTPS and the RTD project-host migration, with requested anchors present.

## Reproduction and limits

[The audit script](audit_tutorial_links.py) records status, redirects, titles, link occurrences, and HTML fragment presence. Run from `inventory` with requests and beautifulsoup4 installed:

```bash
python audit_tutorial_links.py --report /tmp/fresh-link-audit.json --cache /tmp/metplus-link-audit-pages
```

[Raw link results](fresh-link-audit.json) retain the automated exceptions; [browser follow-up](external-browser-link-validation.json) records the final classifications. Binary endpoints were accessed by streamed GET and closed without downloading full data files. The audit excludes sidebar navigation, email delivery, external pages' onward links, and interactive app behavior. It does not verify scientific correctness, historical runtime compatibility, or every external page's semantic content.

No tutorial text, versions, styles, or link destinations changed in this verification/audit pass. Historical URLs remain intact. A future source-content repair would require verified historical replacements for the three unavailable destinations; this report does not assert that such replacements exist.
