# Keel Stats and StatsNext source review

Checked 2026-11-25. This is a bounded publisher-documentation review, not a
catalog-wide freshness review, authenticated API test, or data-admission decision.
Public pages were readable through the research retrieval service; no account,
MCP connection, paid access, bulk export, or independent recomputation was used.
No numeric HTTP status is inferred from rendered-page retrieval.

## Keel Stats analytical website

Canonical URL: <https://keelstats.com/nfl>.
Credit: @symonovserhii, affiliated contributor, [issue #27](https://github.com/JovaniPink/awesome-nfl-data/issues/27)
and [November 22 revision](https://github.com/JovaniPink/awesome-nfl-data/issues/27#issuecomment-7075384344).

The NFL page provides statistical views alongside proprietary outputs. The
[methodology](https://keelstats.com/methodology) distinguishes Keel's EPA,
rankings and projections from underlying game records. Their numerical accuracy
and historical information availability were not independently qualified.

[MCP documentation](https://keelstats.com/mcp) documents limited account-free
access, generally current/previous seasons and games within two weeks of today,
with tool-specific differences. Free accounts expand history and Pro provides
additional functionality. No MCP call was executed. [Use our data](https://keelstats.com/press)
permits credited editorial use of Keel-created numbers/charts but withholds raw
downloads and bulk exports; [terms](https://keelstats.com/terms), updated November
8, restrict bulk copying, scraping and resale. Upstream feed rights are separate.

Decision: include as an analytical website with bounded access/reuse wording.
No raw-feed, unrestricted-reuse or model-performance claim is established.

## StatsNext positional statistics

Canonical URL: <https://statsnext.com/nfl/defense-vs-position>.
Credit: @CatalystPit, disclosed owner, [issue #28](https://github.com/JovaniPink/awesome-nfl-data/issues/28).

The page displayed regular-season per-game allowances to listed QB, RB, WR and
TE positions, sample counts and recent-three-game comparisons. Its coverage ran
through November 23 with a November 24 update date. The publisher describes
summing opposing players' box-score results at their listed position, then
averaging over the defense's games. Small samples and opponent mix constrain
interpretation. These are historical summaries, not predictions; no opponent or
pace adjustment is established for these per-game figures.

The page's citation notice allows free reading/linking, requests source URL and
update-date attribution for figures, and does not authorize redistribution.
[Terms](https://statsnext.com/terms), effective October 15, 2026, exclude API,
bulk-download, resale and commercial redistribution from consumer access; a
separate written agreement is needed for data arrangements. This entry concerns
statistical reference tables within a broader betting-research product.

Decision: include as an analytical website. No API, export, open-data grant or
independently verified accuracy is claimed.

## Metadata and validation boundary

Both canonical URLs are first added on 2026-11-25. Existing creation dates and
historical catalog review/projection dates remain unchanged. Regenerate the
index from the README and run all contributing.md checks. No source-audit TSV or
source matrix exists in this repository; this dated review records the evidence.

Material AI assistance: research, original summaries and implementation were
prepared with an AI assistant; claims are bounded by the linked publisher pages.
