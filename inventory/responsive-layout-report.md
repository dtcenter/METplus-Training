# Responsive layout follow-up

Authorized 2026-10-23 after commit `e745ace`. Scope: confirm the earlier-chapter deployment, remove page-level horizontal overflow, and preserve historical tutorial content.

## Published deployment check

All 14 published chapter bodies match the `e745ace` comparison build. The four earlier chapters' published RST source files also match the committed repairs. All 69 checked resource/navigation URLs loaded and checked internal anchors resolved. Two initially stale HTML responses matched on a fresh fetch. See [deployment evidence](earlier-repair-deployment-validation.json).

## Changes

The shared documentation stylesheet now applies these rules through 1100 pixels, covering both phones and the narrow desktop layout with its sidebar:

- Long identifiers and filenames can wrap in prose.
- Commands and output retain preformatted whitespace and scroll horizontally within their blocks.
- Wide math and tables scroll within their containers.

The rule overrides the existing table-container `overflow: visible !important` where necessary. Wider desktop styles are unchanged. The shared rule also applies to other documentation pages at these widths; the documentation home, tutorial index, and training-series index were checked alongside the 14 chapters.

The deployment/content comparison additionally exposed an error in the preceding emphasis normalization: four 40-asterisk separators had been removed from a Preliminary Work sample log. They are restored exactly as in Drupal, and that log is rendered as a literal block. The earlier-chapter validator now preserves literal asterisk runs during normalization and checks their rendered presence, preventing the previous check from silently accepting that loss. Three shifted CSV mapping locations were refreshed. No instructions, versions, external URLs, or exercise behavior were changed.

## Validation

- Firefox 158.0.1 checked all 14 chapters and three index pages at widths 320, 390, 767, 768, 769, 1024, 1100, 1101, and 1280: **153 page/width cases, zero page-level overflows, zero broken images, and zero failed horizontal-scroll tests**. A 1000-pixel viewport height was used.
- The statistics review was additionally checked after MathJax's startup promise completed: all 17 equations rendered, with no page overflow at 390, 769, or 1280 pixels.
- Narrow-screen table and code/output samples were visually inspected, including their scrollbars. This is a sampled visual review, not an inspection of every screen position or every interaction.
- The pinned Sphinx 8.2.3 / sphinx-rtd-theme 3.0.1 comparison build passes `-E -W --keep-going` with zero warnings/errors. As before, autodoc remains enabled and intersphinx is excluded; this is not a full recreation of every docs dependency.
- All earlier-chapter preservation checks, the 551-block conversion fidelity checks for Sessions 3–11/survey, and the 65-element / 182-span emphasis checks pass. `git diff --check` passes.

Evidence: [responsive browser results](responsive-layout-validation.json), [earlier-chapter checks](early-chapter-validation.json), and [conversion regression](responsive-conversion-validation.json). Screenshots are temporary artifacts in `/tmp/metplus-responsive-browser` and `/tmp/metplus-responsive-math` and are not committed.

The original outstanding-link list and the two inaccessible external source URLs remain separate from this layout work. The checks above describe the local responsive build; the initial deployment check establishes publication of `e745ace`, not of this subsequent CSS change.
