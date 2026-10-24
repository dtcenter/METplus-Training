# Earlier-chapter diagnostic repair and browser review

Authorized in the conversation on 2026-10-23. Baseline: `1947d82`. Scope: Basic Verification Statistics Review, Preliminary Work, Grid-to-Grid, and Grid-to-Obs. The original outstanding-link list remains unavailable; no replacement link audit or external destination changes are included.

## Repairs

- Corrected empty/malformed directives and indentation, including Plot-Data-Plane usage, PB2NC usage, hints, and nested lists. Corrected `code_block` to `code-block` and the malformed third list-item marker.
- Rendered configuration snippets and sample output as literal content within their existing callouts. Retained source bold spans in sample output using `parsed-literal`; tutorial-format explanations remain prose.
- Recovered escaped comparison operators, ampersands, shell continuation line breaks, Python `<module>` text, and leaked HTML formatting tags.
- Repaired strong-emphasis boundaries without changing the wording.
- Converted conflicting inline links (HK, HSS, Natural Earth, and “here”) to anonymous references, retaining every original URL and visible label.
- Repaired the existing probability-discussion target from a comment to an explicit Sphinx label; the referring link now resolves locally. Existing explicit labels are retained.
- Refreshed 58 shifted line locations in the 171-page CSV mapping.

Historical component versions, exercise instructions, command tokens, and source defects remain. For example, the statistical review's literal `<\br>` text is present in Drupal itself and is preserved; this pass does not silently repair source instructions. No practical commands were executed.

## Validation

The pinned Sphinx 8.2.3 / sphinx-rtd-theme 3.0.1 comparison build passes with `-E -W --keep-going`: **zero warnings or errors**, down from the 61 recorded diagnostics in these chapters. As in earlier comparison builds, autodoc is enabled and intersphinx is excluded to avoid an unrelated remote inventory dependency; this is not a full recreation of every documentation dependency.

[Earlier-chapter checks](early-chapter-validation.json), reproduced with [validate_early_chapters.py](validate_early_chapters.py), confirm:

- Text is unchanged after explicitly accounting for recovered HTML entities/tags, emphasis delimiters, directive markup, anonymous-reference syntax, the list-item marker, and whitespace. The comparison preserves other punctuation and operators.
- Heading text/order, all external URLs, and existing explicit labels are unchanged.
- No rendered system messages or literal strong-emphasis markers remain in prose; checked internal pages/anchors resolve.

Sessions 3–11 and the survey also pass their original fidelity validator, and all 65 prior emphasis repairs / 182 bold spans pass the emphasis validator. `git diff --check` passes. These checks establish conversion preservation for the edits, not a new exhaustive source audit of the four earlier chapters or runtime correctness.

Reproduction from the repository root:

```bash
python -m sphinx -E -W --keep-going -b html -D extensions=sphinx.ext.autodoc docs /tmp/metplus-early-html > /tmp/metplus-early-build.log 2>&1
python inventory/validate_early_chapters.py --html /tmp/metplus-early-html --log /tmp/metplus-early-build.log
python inventory/validate_conversion.py --source /tmp/metplus-v5-drupal.html --html /tmp/metplus-early-html --log /tmp/metplus-early-build.log
python inventory/validate_emphasis.py --source /tmp/metplus-v5-drupal.html --html /tmp/metplus-early-html
```

## Published and visual review

The ten published chapters (Sessions 3–11 and survey) match the local emphasis-fix build from `1947d82`. The 36 previously checked resource/navigation URLs still load and their checked internal anchors resolve. See [deployment results](published-emphasis-deployment-validation.json). Earlier-chapter repairs were reviewed locally before deployment.

Firefox 158.0.1 provides usable rendering on this host, resolving the earlier Chrome screenshot limitation. Desktop (1280 × 1000) and narrow-window (390 × 1000) samples were inspected for all 14 chapters: chapter tops, first table/callout, and first callout literal. Figures load, callout colors and literal formatting render, and sampled desktop layout is usable. This sampled review does not cover every section or every interaction in these long chapters. Browser dimensions, image checks, and screenshot names are saved in [browser-review-validation.json](browser-review-validation.json); screenshots remain temporary local artifacts.

**Remaining responsive issue:** nine chapters exceed the 390-pixel viewport width. Published Sessions 3, 4, 5, 7, and 9 measure 411, 457, 423, 429, and 423 pixels respectively. The four local earlier chapters measure 564, 494, 646, and 518 pixels respectively (statistics review, preliminary work, Grid-to-Grid, Grid-to-Obs). Long bold filenames demonstrably extend beyond the viewport in Sessions 3, 4, and 2; other overflow also needs element-level investigation. This is page-level horizontal overflow, separate from expected scrolling within long code/output blocks. Proposed follow-up: a separately scoped responsive CSS/layout pass that wraps long prose identifiers and contains wide tables/math while preserving horizontally scrollable literals. Shared styles are unchanged in this diagnostic pass.

The two inaccessible external source destinations and historical exercise/runtime limitations recorded in the completion report remain unchanged.

## Responsive follow-up and literal-separator correction

The earlier-chapter repairs are now confirmed in published HTML and source files. The subsequent [responsive pass](responsive-layout-report.md) resolves the recorded page-level overflow locally, including the narrow desktop/sidebar breakpoint. That pass also restores four literal log separators lost during this report's earlier formatting pass; the strengthened validator preserves and checks those asterisk runs. The original validation had normalized them away and therefore did not detect the loss. Historical sample output is now restored, and the current checks pass.
