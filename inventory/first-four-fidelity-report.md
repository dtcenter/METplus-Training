# First-four-chapter source fidelity and final build

Authorized after `83517df`. Historical source: the original Drupal export, SHA-256 `dae5e36c70f1078c34f83b83826b0518a6827351ef281988915d808866507417`. This follows the earlier diagnostic-only pass and completes the requested source comparison for Basic Verification Statistics Review, Preliminary Work, Grid-to-Grid, and Grid-to-Obs.

## Source comparison

| Chapter | Drupal pages | Source code/output/legend blocks | Source links | Prose/callout units | Source image occurrences |
|---|---:|---:|---:|---:|---:|
| Statistics review | 21 | 50 | 103 | 263 | 49 |
| Preliminary work | 17 | 113 | 33 | 258 | 0 |
| Grid-to-Grid | 25 | 103 | 26 | 320 | 1 |
| Grid-to-Obs | 22 | 118 | 36 | 389 | 1 |
| Total | 85 | 384 | 198 | 1,230 | 51 |

[The source validator](validate_first_four_fidelity.py) checks ordered literal coverage and reverse coverage to catch added characters; the actual command/output checks preserve punctuation/operators while ignoring whitespace. Of the 384 source blocks, 383 are checked as literals. The remaining block is the overview's gray-box color legend, already adapted to the purple Sphinx callouts and represented as explanatory prose. The validator also checks source-link occurrence counts, prose/callout coverage, unchanged heading text/order, image identities/files/alternative text, native representations, all seven source usage tables, and build diagnostics. [Results](first-four-fidelity-validation.json) contain no errors.

The apparent 22-image shortfall in the statistics chapter consists of **17 equations and five tables already represented natively**. Their original assets were visually compared with the native content; the blank cells in the original contingency-table images are intentional. [The representation map](first-four-native-representations.json) records the expected LaTeX and table cells. The existing C2 shorthand uses explicitly defined FA/CR terms. No duplicate images were added and no image bytes changed.

Presentation adaptations are explicit: admonition titles replace leading “NOTE”/“IMPORTANT NOTE” text; the overview's colors describe the Sphinx theme; descriptive hyperlink labels may replace raw displayed URLs; and [the link policy](first-four-link-policy.json) records local section aliases and the previously authorized historical documentation versions. Prose checks normalize case, punctuation, and whitespace; they do not establish scientific correctness. Neither exercise commands nor literal operators are normalized by those link/prose policies.

## Repairs

- Restored source wording in three statistical call-to-action links and an appendix label; corrected a native table's accidental “2xw” caption to “2x2”.
- Removed a stray zero after a threshold list, a stray `=` after a shell continuation, a stray ampersand after a Python filename, and a stray `<` after a configuration directory. Restored the source's comment separator and `.txt` / `.stat` output filename endings.
- Recovered the original Natural Earth download command from malformed link markup. Restored `GAC.poly` exactly as written in Drupal; this does not assert that the historical data path exists today.
- Restored clickable setup-script, shapefile, and Intel links inside literal output without changing copied text. The four restored external endpoints returned HTTP 200 in streamed checks; full binary files were not downloaded. See [link results](first-four-restored-link-validation.json).
- Corrected an accidentally literal-rendered note and restored six flattened tool-usage tables. [All seven usage-table fixtures](first-four-usage-tables.json), including the existing PCP-Combine table, match the source cells.
- Restored the source's binary-solutions reference target and a lost timing-control link; added its local label. Filled empty image alternatives with descriptions. Existing headings and explicit labels are retained.
- Refreshed 48 shifted mapping line locations. The original inventory JSON remains a baseline snapshot.

The validator was also run against a temporary HTML copy with the former trailing-zero defect deliberately reintroduced; reverse literal coverage correctly rejected it. No test mutation affected repository files.

## Full build: step two complete

A clean Python **3.12.15** environment installed every exact requirement in `docs/requirements.txt`: Pillow 12.3.0, Sphinx 8.2.3, sphinx-copybutton 0.5.2, sphinx-design 0.6.1, sphinx-gallery 0.19.0, and sphinx-rtd-theme 3.0.1. `pip check` reported no broken requirements.

The strict build used **the unmodified project configuration, without extension overrides**:

```bash
python -m sphinx -E -W --keep-going -b html docs /tmp/metplus-full-html
```

Result: **zero warnings/errors**. Autodoc and intersphinx remained enabled. The configured NumPy inventory URL redirected successfully to `https://numpy.org/doc/stable/objects.inv`; the configuration was not changed to bypass the remote dependency. [Build evidence](full-build-validation.json) records installed pins, configuration/requirements hashes, command, and inventory messages; [the environment freeze](full-docs-environment.txt) records transitive dependencies. This was a local macOS build with Python 3.12 and the exact requirements, not a recreation of RTD's Ubuntu 22.04 container.

The source validator above and the existing Sessions 3–11/survey validator both pass against this full build. The latter checks 551 literal blocks, 95 link occurrences, 23 figures, and 823 prose units; see [full-build regression results](full-build-conversion-validation.json). All 65 emphasis-repair elements / 182 spans also pass.

Firefox checks of the four repaired chapters at widths 390, 769, and 1280 produced 12 passing cases, with no page-level overflow, broken images, or failed horizontal scroll tests. Restored table and literal samples were visually inspected after MathJax startup. See [browser results](first-four-browser-validation.json). Screenshots remain temporary under `/tmp/metplus-fidelity-browser`. This is sampled visual verification, not a review of every scroll position.

## Handoff

The source review and full configured build are complete. The three unavailable historical documentation destinations remain deliberately deferred: Navy ATCF `abdeck.txt`, GFDL Vortex Tracker downloads, and the NWP Containers tutorial. The requested reminder was delivered immediately after step two passed. No mirrors or modern replacements were substituted.

The branch is ready for final maintainer review and merge/handoff. This pass does not merge branches, execute historical MET exercises, or create AWS resources. The previously published responsive release was verified separately; the source-fidelity repairs in this pass still need the normal RTD rebuild after push.

To reproduce the final comparisons, install requests/beautifulsoup4 separately for audit tooling (they need not be added to the pinned build environment), supply the original export, then run:

```bash
python inventory/validate_first_four_fidelity.py --source /tmp/metplus-v5-drupal.html --html /tmp/metplus-full-html --log /tmp/metplus-full-build.log --report /tmp/first-four-fidelity.json
python inventory/validate_conversion.py --source /tmp/metplus-v5-drupal.html --html /tmp/metplus-full-html --log /tmp/metplus-full-build.log
python inventory/validate_emphasis.py --source /tmp/metplus-v5-drupal.html --html /tmp/metplus-full-html
```
