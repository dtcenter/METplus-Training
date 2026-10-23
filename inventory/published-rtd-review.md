# Published RTD review

Reviewed 2026-10-23 against local commit `c869fff4e05a3932eb72883706839736eb6fe00d`.

Scope: Sessions 3–11 and Tutorial Survey on the published `feature_69_drupal2rtd_auto` version. The legacy hostname redirects to the [METplus Training subproject](https://metplus.readthedocs.io/projects/metplus-training/en/feature_69_drupal2rtd_auto/Tutorial/v5.0/Session_3_Analysis_Tools.html).

## Findings

**Remaining emphasis conversion defects:** literal `**` markers occur in 65 prose paragraphs/list items. Some parsed bold spans also extend across unintended text. These defects are present in both published HTML and the validated local output, so text equality and a warning-free scoped build did not detect them. The completion report's emphasis-repair statement should not be read as exhaustive.

| Session | Affected prose paragraphs/list items |
|---|---:|
| 3 | 10 |
| 4 | 5 |
| 5 | 8 |
| 6 | 4 |
| 7 | 4 |
| 8 | 10 |
| 9 | 23 |
| 10 | 1 |
| 11 and survey | 0 |

Examples:

- [Session 3](https://metplus.readthedocs.io/projects/metplus-training/en/feature_69_drupal2rtd_auto/Tutorial/v5.0/Session_3_Analysis_Tools.html): environment verification displays `MET_BUILD_BASE **` and `**${MET_BUILD_BASE}/bin`; the run_metplus.py/PATH instruction also exposes emphasis delimiters.
- [Session 9](https://metplus.readthedocs.io/projects/metplus-training/en/feature_69_drupal2rtd_auto/Tutorial/v5.0/Session_9_Python_Embedding.html): the Python installation explanation and numbered command elements expose delimiters around tool names and labels.
- [Session 10](https://metplus.readthedocs.io/projects/metplus-training/en/feature_69_drupal2rtd_auto/Tutorial/v5.0/Session_10_Subseasonal_to_Seasonal_S2S.html): `fcst_OMI_comp_phase.png ** and ** obs_OMI_comp_phase.png` appears in prose.

All affected text and its section identifier are listed in [published-rtd-validation.json](published-rtd-validation.json). Counts exclude literal code blocks; they count affected prose elements, not individual delimiters. This scan does not establish that every other inline-markup defect has been found.

**Visual review remains incomplete:** Chrome produced another blank screenshot and macOS CVDisplayLink errors. This does not establish that the published page is blank. Page layout, scrolling, responsive behavior, and visual clipping still require a working browser review.

## Successful checks

- All ten published chapter bodies match the validated local HTML after extracting visible body text and normalizing whitespace through BeautifulSoup's text extraction. This confirms text parity, not an independently verified RTD build commit.
- All 551 literal blocks, 23 image occurrences, and seven tables are present in the published chapter bodies. No rendered Sphinx system-message elements were found.
- All 36 unique checked URLs for document images, stylesheets, scripts, and in-body internal navigation returned success. All fragments on checked internal links exist in their destination HTML. This is an HTTP/HTML check, not evidence that scripts executed or images painted correctly.
- External exercise destinations were not re-audited. The two documented source exceptions (Navy ATCF and MET-Help archive) remain as recorded in the completion report.

## Proposed follow-up scope

1. Repair emphasis boundaries in Sessions 3–10 by comparison with Drupal, preserving prose, commands, historical component versions, and exercise behavior. Rebuild, check the resulting strong spans and literal delimiters, and rerun fidelity validation. This review makes no chapter edits.
2. Complete a desktop and narrow-window browser review when rendering is available, focusing on long commands, tables, callouts, figures, and section navigation.
3. For the four protected chapters, propose a separate conversion-only pass covering the 61 recorded build diagnostics: malformed/empty directives, indentation and list structure, duplicate targets, inline markup, escaped content, and the undefined `metplus_sol_prob_fcst_verif` reference. Compare each correction with the historical source and audit affected internal targets. Preserve content and versions. Do not substitute new destinations for an unspecified outstanding-link list; that original list still needs to be supplied or explicitly replaced by a newly scoped link audit. No protected chapter edits are included in this review.

## Emphasis repair follow-up

The 65 affected prose elements in Sessions 3–10 have now been repaired. Only emphasis boundaries and adjacent spacing changed; historical wording, versions, commands, headings, and protected chapters remain unchanged.

The rebuilt HTML contains no literal `**` markers in scoped prose. The [emphasis validator](validate_emphasis.py) checks all 65 repaired elements and their 182 bold spans against the RST and the downloaded Drupal snapshot; all pass. This includes retaining a long bold span in Session 8's `point_stat` explanation because Drupal itself emphasizes that entire span. The [results](emphasis-validation.json) contain no errors.

The original conversion fidelity checks also pass: 551 literal blocks, 23 figure occurrences, 95 source-link occurrences, and 823 prose units. See [fresh conversion results](emphasis-conversion-validation.json). The pinned Sphinx/theme build still reports 61 diagnostics, all confined to protected chapters, with none in Sessions 3–11 or the survey. `git diff --check` passes. The original published-page audit above remains a historical checkpoint; these follow-up results describe the rebuilt local HTML, not a visual review or a post-deployment RTD check.

## Authorized follow-up completed

The emphasis repair is now confirmed in the published chapter HTML. Firefox also enabled sampled visual checks at desktop and narrow widths. The subsequently authorized earlier-chapter diagnostic pass resolves the 61 recorded diagnostics locally. A remaining narrow-window overflow issue affects nine sampled chapters; details and scope limitations are in [the follow-up report](early-chapter-repair-report.md). The original findings above are historical checkpoints.
