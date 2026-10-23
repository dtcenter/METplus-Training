# METplus v5.0 conversion inventory

Inventory date: 2026-10-23. Scope: mapping and static inventory only; no tutorial edits, build, link validation, or full content comparison.

Git baseline: `6e9847fe7aa336f2b2b71e5fa20bd4a3570489d3`. The pre-existing untracked `AGENTS.md` was left unchanged.

## Source and mapping method

Source: [Drupal full-book export](https://dtcenter.org/book/export/html/1595), downloaded during this inventory. Export SHA-256: `dae5e36c70f1078c34f83b83826b0518a6827351ef281988915d808866507417`.

171 Drupal book pages map to 15 local RST files. File assignments follow the Drupal chapter URL prefixes and local toctree order. 154 page locations match normalized heading titles in source order; 17 have title variants or inline text and are labeled as candidates in the CSV. Matching titles establish structural correspondence, not content completeness. Repeated headings such as Configure, Run, and Output are disambiguated by source order; final anchor targets still require validation.

## Chapter inventory

| Local file | Drupal pages | RST lines | URL occurrences | Moving URLs | Image directives / source images | Escaped entities |
|---|---:|---:|---:|---:|---:|---:|
| index.rst | 1 | 32 | 0 | 0 | 0 / 0 | 0 |
| Basic_Verification_Statistics_Review.rst | 21 | 1705 | 70 | 0 | 27 / 49 | 40 |
| Preliminary_work_METplus_setup.rst | 17 | 1590 | 24 | 0 | 0 / 0 | 19 |
| Session_1_Grid-to-Grid.rst | 25 | 1753 | 19 | 0 | 1 / 1 | 62 |
| Session_2_Grid-to-Obs.rst | 22 | 1941 | 28 | 0 | 1 / 1 | 19 |
| Session_3_Analysis_Tools.rst | 13 | 1209 | 8 | 0 | 0 / 2 | 574 |
| Session_4_Ensemble_and_PQPF.rst | 15 | 1467 | 10 | 7 | 0 / 1 | 643 |
| Session_5_MODE_and_MTD.rst | 12 | 1223 | 2 | 1 | 0 / 1 | 335 |
| Session_6_Track_and_Intensity.rst | 15 | 1325 | 6 | 1 | 0 / 1 | 444 |
| Session_7_Feature_Relative_Use_Cases.rst | 4 | 433 | 0 | 0 | 0 / 0 | 6 |
| Session_8_METplus_Analysis_Tools.rst | 11 | 1445 | 16 | 2 | 5 / 5 | 32 |
| Session_9_Python_Embedding.rst | 8 | 651 | 0 | 0 | 5 / 5 | 0 |
| Session_10_Subseasonal_to_Seasonal_S2S.rst | 4 | 299 | 0 | 0 | 3 / 3 | 0 |
| Session_11_METplus_Cloud.rst | 2 | 207 | 0 | 0 | 5 / 5 | 4 |
| Tutorial_Survey.rst | 1 | 23 | 0 | 0 | 0 / 0 | 0 |

Counts are static indicators, not confirmed defects. URL counts include escaped HTML URLs and omit links whose targets were lost. Moving URLs match /latest/, /develop/, /main/, or /master/; all 11 detected occurrences currently use /latest/. Entity counts cover &lt;, &gt;, &amp;, and &nbsp;. Source image occurrences can include repeated images; a count difference does not establish missing instructional content. No figure directives were found.

## Findings and concerns

- All Drupal chapter groups have corresponding local files. No wholly unassigned Drupal pages were found; detailed content completeness remains unverified.
- Session 4 answers exist at line 1425 as bold text rather than a section heading. Do not interpret the heading-count difference as missing answers or change the completed hierarchy without review.
- Session 7 uses shortened Feature Relative Init and Lead headings; Session 6 distinguishes two Drupal Run on TC-Pairs output pages as Filter and Summary. These are mapping aliases, not requests to rename headings.
- Sessions 3–6 have 2, 1, 1, and 1 Drupal image occurrences respectively, but zero local image directives. Inspect for escaped image markup or omissions.
- Sessions 3–6 account for 1,996 of the 2,178 counted escaped entities. Session 4 contains escaped HTML tags and unindented directive bodies, so fixing entities alone will not restore correct structure.
- Session 7 contains links such as MET Users Guide and Instance Names in the Process List without explicit destinations. Several later chapters have zero literal URLs despite source links. Session 9 has one source link, Session 10 six, and the survey seven. A URL-only link checker will miss these losses.
- Eleven literal latest URL occurrences remain: Session 4 seven, Session 5 one, Session 6 one, and Session 8 two. Destinations and allowed historical branches still require individual verification.
- Earlier completed chapters also contain static flags (entities and source/local image count differences). These are recorded only; keep those chapters protected except for the user-supplied outstanding link list.
- The outstanding-link list referred to as To Do in the original request has not been supplied.
- Existing note/important and titled Sample Output/File Contents admonitions, with custom lavender styling in docs/_static/custom.css, are the formatting reference.
- Source errors must be distinguished from conversion errors. For example, Session 11 opens with a statement about feature relative use cases; check Drupal before proposing a correction.

## Next work

1. Resolve the 17 title-variant/inline-text candidate mappings, validate anchor identities, and inspect image discrepancies. Preserve existing titles and chapter structure.
2. Audit links in Sessions 3–11 and the survey, including destinationless link labels and escaped HTML anchors. Apply the user-approved historical version ranges; do not modernize exercises.
3. Start detailed conversion cleanup with Session 3 as a representative batch; Sessions 4–6 are likely the heaviest formatting work.
4. Build and inspect rendered results during correction batches. This inventory did not run Sphinx or validate remote destinations.

## Continuity and scope

Completed sections: Basic Verification Statistics Review, Preliminary Work, Session 1, and Session 2; only explicitly listed outstanding links may be edited there. All chapter/subchapter structure is already completed. Goal: preserve v5.0.0 instructional content and commands, not update component versions.

Files: drupal-to-sphinx.csv contains every source page URL and local line candidate; tutorial-inventory.json contains per-file counts. These artifacts provide a handoff for a new session. A new session is not needed now; starting one at a completed batch boundary is reasonable. Carry forward this report, the user constraints, and any unresolved decisions. The raw Drupal download is temporary at /tmp/metplus-v5-drupal.html and is not a durable repository artifact.
