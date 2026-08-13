# Awesome NFL Data & Analysis [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of up-to-date NFL data sources, analytics sites, APIs, tools, film study, and low-noise podcasts. Each item includes a short description and a reliable URL.

Last reviewed: August 2026.

## Contents

- [Official & League Data](#official--league-data)
- [Open Data & APIs](#open-data--apis)
- [Analytics, Charting & Tracking](#analytics-charting--tracking)
- [Historical Research](#historical-research)
- [Contracts, Injuries & Transactions](#contracts-injuries--transactions)
- [Data Analysis Libraries & Tools](#data-analysis-libraries--tools)
- [YouTube & Film Study](#youtube--film-study)
- [Podcasts](#podcasts)
- [Metrics & Methods](#metrics--methods)
- [Legacy / Archived](#legacy--archived)
- [Choosing a Data Stack](#choosing-a-data-stack)

---

## Official & League Data

League-operated sources. Use these first for official schedules, statistics, designations, transactions, rules, and the NFL's published tracking-derived metrics.

- [NFL Scores & Statistics](https://www.nfl.com/stats/) - Official player and team leaderboards, schedules, standings, and game results.
- [Next Gen Stats](https://nextgenstats.nfl.com/) - Public dashboards for selected tracking-derived metrics such as completion probability, expected rushing yards, separation, and time to throw. This is not the raw tracking feed.
- [Next Gen Stats: How It Works](https://operations.nfl.com/gameday/technology/nfl-next-gen-stats/) - NFL Football Operations overview of the RFID tracking system, collection frequency, and metric types.
- [NFL Big Data Bowl](https://operations.nfl.com/programs-initiatives/innovation/big-data-bowl/) - Annual analytics competition using bounded releases of traditional and Next Gen Stats data; the best official entry point for public tracking-data research.
- [NFL Injury Reports](https://www.nfl.com/injuries/) - Official practice participation and game-status designations by week.
- [NFL Transactions](https://www.nfl.com/transactions/) - Official trades, signings, reserve-list moves, waivers, and terminations.
- [NFL Rulebook](https://operations.nfl.com/the-rules/nfl-rulebook/) - Current playing rules and definitions.
- [NFL Player Health & Safety Injury Data](https://www.nfl.com/playerhealthandsafety/health-and-wellness/injury-data/injury-data) - League-published, aggregate injury trends and annual summaries; distinct from weekly player designations.

## Open Data & APIs

Programmatic and bulk access for research. Check dataset-specific licenses, update schedules, rate limits, and commercial-use terms before redistributing data.

- [nflverse](https://nflverse.nflverse.com/) - The open-source NFL analytics ecosystem and the best starting point for public play-by-play, rosters, schedules, player stats, and related datasets.
- [nflverse-data](https://github.com/nflverse/nflverse-data) - Current automated releases and machine-readable files behind much of the nflverse ecosystem; retain retrieval timestamps and hashes because a release URL alone is not immutable artifact identity.
- [nfldata](https://github.com/nflverse/nfldata) - Schedules, game results, team metadata, and consolidated historical betting lines; treat its market fields as closing proxies rather than authenticated sportsbook snapshots.
- [nflverse Data Update and Availability Schedule](https://nflreadr.nflverse.com/articles/nflverse_data_schedule.html) - Official refresh cadence, correction timing, automation status, source changes, and known availability gaps for nflverse datasets.
- [nflreadpy](https://nflreadpy.nflverse.com/) - Current Python loader for nflverse data. Returns Polars DataFrames and supports caching; preferred over the deprecated `nfl_data_py` package.
- [nflreadr](https://nflreadr.nflverse.com/) - R package for downloading play-by-play and the broader nflverse dataset catalog, with data dictionaries and update-status documentation.
- [nflfastR](https://www.nflfastr.com/) - R package and methodology hub for cleaning play-by-play and computing expected points and win probability fields used across nflverse.
- [SportsDataIO NFL API](https://sportsdata.io/developers/api-documentation/nfl) - Commercial HTTP API for scores, statistics, play data, fantasy, projections, odds, news, and images; access depends on the purchased feed.
- [Sportradar NFL API](https://developer.sportradar.com/football/docs/nfl-ig-api-basics) - Licensed B2B REST feeds for production applications that need structured schedules, rosters, statistics, and play-by-play with vendor support.

## Analytics, Charting & Tracking

These sources add models, human classifications, grades, or tracking-derived fields. Their outputs are not interchangeable with directly observed play-by-play facts.

- [FTN Data](https://ftnfantasy.com/data) - Paid NFL charting and APIs covering play-by-play plus contextual fields such as routes, motion, personnel, coverage, and pressure; also offers DVOA data.
- [SūmerSports](https://sumersports.com/) - Scheme- and roster-oriented analytics, including personnel, formation, and tracking-derived football classifications.
- [PFF NFL](https://www.pff.com/nfl) - Subscription player grades, advanced statistics, and position-specific charting. Grades are evaluations produced by PFF's framework, not physical measurements.
- [Sports Info Solutions Football](https://www.sportsinfosolutions.com/football/) - Professional NFL and college charting, advanced metrics, and commercial data feeds, including Total Points.
- [RBSDM](https://rbsdm.com/stats/stats/) - Public EPA-based team and player dashboards built from play-by-play data.
- [nfelo](https://www.nfeloapp.com/) - Elo ratings, team tiers, quarterback adjustments, game projections, and model-focused NFL analysis.
- [ESPN Analytics](https://www.espn.com/analytics/) - Public analytical models and explainers, including blocking and pass-rush win-rate work; availability varies by season and feature.

## Historical Research

- [Pro Football Reference](https://www.pro-football-reference.com/) - Deep historical player, team, game, draft, award, and conventional-stat reference.
- [Stathead Football](https://stathead.com/football/) - Paid query tools for player, team, game, drive, streak, and play research.
- [The Football Database](https://www.footballdb.com/) - Historical standings, scores, player statistics, and team records; useful as a secondary reference.
- [Pro Football Archives](https://www.profootballarchives.com/) - Long-run professional-football records, rosters, standings, and results extending beyond the modern NFL.

## Contracts, Injuries & Transactions

- [Over the Cap](https://overthecap.com/) - NFL-specific contracts, guarantees, cap space, dead money, restructures, valuations, and future obligations.
- [Spotrac NFL](https://www.spotrac.com/nfl/) - Contract and multi-year cap tables that are useful for cross-checking reported terms and comparing positions.

Use the official injury and transaction sources listed above for weekly designations and roster
moves. Contract details often arrive incrementally. Preserve the source and an `as_of` timestamp,
and reconcile reported terms rather than silently replacing one vendor's representation with
another.

## Data Analysis Libraries & Tools

- [nflplotR](https://nflplotr.nflverse.com/) - Helpers for using NFL team logos, player headshots, wordmarks, and field visualizations with ggplot2.
- [nfl4th](https://www.nfl4th.com/) - Fourth-down decision modeling and analysis in R.
- [Polars](https://pola.rs/) - Fast DataFrame engine used by nflreadpy.
- [DuckDB](https://duckdb.org/) - Embedded analytical database well suited to querying Parquet and joining NFL datasets locally.

## YouTube & Film Study

High-signal channels that teach scheme, technique, scouting, and roster construction rather than relying on debate-show reactions.

- [The QB School](https://www.youtube.com/@TheQBSchool) - Former NFL quarterback J.T. O'Sullivan explains reads, progressions, protections, route concepts, footwork, and defensive rotations with All-22 film.
- [Thinking Football](https://www.youtube.com/@ThinkingFootball) - Polished film essays connecting player execution, offensive structure, defensive answers, and historical context.
- [The Athletic Football Show](https://www.youtube.com/@TheAthleticFootballShow) - League-wide scheme, personnel, coaching, and roster-construction analysis, with selected film-room episodes.
- [Brett Kollmann](https://www.youtube.com/@BrettKollmann) - Detailed film essays on NFL players, prospects, trends, and schematic fit.
- [Bootleg Football](https://www.youtube.com/@BootlegFootball) - Long-form team, draft, scouting, roster, and scheme analysis from Brett Kollmann and E.J. Snyder.
- [Kurt Warner x QBConfidential](https://www.youtube.com/@kurtwarnerqbc) - Advanced quarterback-room analysis of progressions, leverage, coverage indicators, route conversions, timing, and footwork.
- [MatchQuarters](https://www.youtube.com/@MatchQuarters) - Defensive specialist covering split-field coverages, simulated pressures, fronts, personnel, spacing, and pattern-match rules.
- [NFL Films](https://www.youtube.com/@NFLFilms) - League-produced football history and film features; player-led film sessions are especially useful for position technique and responsibility.

## Podcasts

Low-temperature shows where arguments are usually grounded in film, personnel, data, coaching structure, or front-office constraints.

- [The Athletic Football Show](https://podcasts.apple.com/us/podcast/the-athletic-football-show-a-show-about-the-nfl/id1528622068) - Best all-around mix of league-wide scheme, coaching, roster construction, and player evaluation.
- [The Mina Kimes Show featuring Lenny](https://www.espn.com/espnradio/podcast/archive/_/id/2544457) - Accessible weekly analysis of every team's strengths, weaknesses, personnel, and schematic direction.
- [Check the Mic](https://podcasts.apple.com/us/podcast/check-the-mic-with-steve-palazzolo-sam-monson/id1761398472) - High-volume game review, player performance, analytics, and team-building discussion from Steve Palazzolo and Sam Monson.
- [The Bill Barnwell Show](https://www.espn.com/espnradio/podcast/archive/_/id/11046849) - Transactions, contracts, coaching decisions, team-building logic, and analytical skepticism.
- [NFL Daily](https://www.nfl.com/podcasts/nfl-daily) - Frequent league-news layer hosted by Gregg Rosenthal with rotating reporters and analysts; depth varies by episode.
- [Move the Sticks](https://www.nfl.com/podcasts/move-the-sticks) - Former scouts Daniel Jeremiah and Bucky Brooks on evaluation, traits, roster construction, and the draft.
- [Unexpected Points](https://www.unexpectedpoints.com/t/podcast) - Kevin Cole on statistical models, projections, positional value, draft value, and testing conventional assumptions.

## Metrics & Methods

- [nflfastR Models](https://opensourcefootball.com/posts/2020-09-28-nflfastr-ep-wp-and-cp-models/) - Documentation for expected points, win probability, completion probability, expected yards after catch, and expected-pass models.
- [nflverse Play-by-Play Dictionary](https://nflreadr.nflverse.com/articles/dictionary_pbp.html) - Field definitions for nflverse play-by-play data; consult this before interpreting model columns.
- [FTN DVOA](https://ftnfantasy.com/dvoa) - Opponent- and situation-adjusted team efficiency rankings and articles; full data access may require a subscription.
- [Pro Football Reference Glossary](https://www.pro-football-reference.com/about/glossary.htm) - Definitions for conventional and advanced fields used throughout the site.

## Legacy / Archived

Useful for reproducibility and historical work, but not recommended as the default for a new project.

- [nflverse-data-archives](https://github.com/nflverse/nflverse-data-archives) - Point-in-time and legacy nflverse release files for reproducibility and as-of research; archive snapshots overlap heavily and must not be concatenated as independent training observations.
- [FiveThirtyEight NFL Elo](https://github.com/fivethirtyeight/nfl-elo-game) - Static MIT-licensed scores, Elo probabilities, model code, and reader forecasts for historical forecast evaluation; useful as a benchmark rather than a current production feed.
- [nfl_data_py](https://github.com/cooperdff/nfl_data_py) - Deprecated Python package retained for older notebooks; new work should use nflreadpy.
- [Advanced Football Analytics](https://www.advancedfootballanalytics.com/) - Archived essays and early public NFL EPA/WPA work.

## Choosing a Data Stack

| Goal                               | Start with                                  | Add when needed                                        |
| ---------------------------------- | ------------------------------------------- | ------------------------------------------------------ |
| Personal analysis or modeling      | nflverse + nflreadpy/nflreadr               | DuckDB, FTN charting, Pro Football Reference           |
| Scheme and film research           | The QB School + Thinking Football           | MatchQuarters, FTN, SūmerSports                        |
| Historical fact-checking           | Pro Football Reference                      | Stathead, Pro Football Archives                        |
| Contracts and cap analysis         | Over the Cap                                | Spotrac cross-checks and source timestamps             |
| Player-tracking research           | Big Data Bowl releases                      | Public Next Gen Stats derived metrics                  |
| Production scores or live products | Licensed Sportradar or SportsDataIO feed    | nflverse historical enrichment and specialist charting |

Keep these categories distinct in a data model:

| Data layer            | Examples                                                 |
| --------------------- | -------------------------------------------------------- |
| Observed facts        | Down, distance, participants, result, and position.      |
| Human classifications | Routes, coverages, assignments, and pressure sources.    |
| Model outputs         | EPA, win probability, completion probability, forecasts. |
| Evaluations           | Player grades and scouting judgments.                    |
| Market signals        | Odds, lines, and contract reporting.                     |

Retain provenance, metric definitions, licensing, uncertainty, and `as_of` timestamps when combining sources.

An archived release represents what a source published at a particular time, not an additional
football observation. Preserve revisions for correction and leakage research, but select one
declared as-of version when constructing a training or evaluation dataset.

The nflverse data repository is CC-BY-4.0, but individual derived datasets and upstream sources can
carry distinct attribution or usage terms. In particular, preserve the attribution and license
attached to FTN-derived data rather than assuming the repository-level license supersedes it.

---

## Contributing

Spotted a dead link, a better official source, or a high-signal resource? Pull requests are welcome. Keep additions current, specific, and non-promotional; see [contributing.md](contributing.md).

Before opening a pull request, run the dependency-free catalog gate with Python 3.11 or newer:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
```

GitHub Actions runs the same checks on Python 3.11 and the current Python 3.14 line for every pull
request and push to `main`. The validator checks the Contents order and anchors, required files,
relative links, unique HTTPS resource URLs, and entry formatting. A passing result does not prove
that external URLs respond, that a source is still maintained, or that its access and licensing
terms are unchanged; those require human review.
