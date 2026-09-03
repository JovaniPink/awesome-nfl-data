from __future__ import annotations

import re
import tempfile
import unittest
from pathlib import Path
from typing import Final, TypeAlias, TypedDict

from scripts.validate_readme import (
    RESOURCE_ENTRY_RE,
    github_anchor,
    validate_document,
)

CatalogEntry: TypeAlias = tuple[str, str, str]


class ReleaseSourceContract(TypedDict):
    name: str
    url: str
    section: str
    required_phrases: tuple[str, ...]
    forbidden_phrases: tuple[str, ...]


VALID_README = """# Awesome Test [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A focused catalog.

Last reviewed: August 2026.

## Contents

- [Official & League Data](#official--league-data)

## Official & League Data

- [Example](https://example.com/) - Example primary source.

## Contribute

See the contribution guide.
"""

PUBLISHABLE_TEXT_FILES: Final[tuple[str, ...]] = (
    ".github/workflows/validate.yml",
    "AGENTS.md",
    "LICENSE",
    "README.md",
    "code-of-conduct.md",
    "contributing.md",
    "scripts/validate_readme.py",
    "tests/test_validate_readme.py",
)

RELEASE_SOURCE_CONTRACTS: Final[tuple[ReleaseSourceContract, ...]] = (
    {
        "name": "NFL Draft Tracker",
        "url": "https://www.nfl.com/draft/tracker",
        "section": "Official & League Data",
        "required_phrases": (
            "Official draft selections and prospect profiles",
            "reported measurements",
            "Next Gen Stats scores",
            "human analyst evaluations",
            "keep these field types distinct",
            "not a bulk-data license",
        ),
        "forbidden_phrases": ("is a bulk-data license",),
    },
    {
        "name": "NFL Scouting Combine",
        "url": "https://www.nfl.com/combine",
        "section": "Official & League Data",
        "required_phrases": (
            "Official participant and prospect surface",
            "combine measurements and workout results",
            "does not establish bulk retrieval or redistribution rights",
        ),
        "forbidden_phrases": (
            "establishes bulk retrieval or redistribution rights",
        ),
    },
)


def _catalog_entries_by_url(text: str) -> dict[str, CatalogEntry]:
    entries: dict[str, CatalogEntry] = {}
    section = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line.removeprefix("## ")
            continue
        match = RESOURCE_ENTRY_RE.fullmatch(line)
        if match and match.group(3):
            entries[match.group(2)] = (match.group(1), section, match.group(3))
    return entries


def _release_source_contract_errors(text: str) -> tuple[str, ...]:
    errors: list[str] = []
    entries = _catalog_entries_by_url(text)
    for contract in RELEASE_SOURCE_CONTRACTS:
        url = contract["url"]
        entry = entries.get(url)
        if entry is None:
            errors.append(f"missing release source URL: {url}")
            continue
        name, section, description = entry
        if name != contract["name"]:
            errors.append(f"unexpected README name for {url}: {name}")
        if section != contract["section"]:
            errors.append(f"unexpected README section for {url}: {section}")
        for phrase in contract["required_phrases"]:
            if phrase not in description:
                errors.append(f"missing README phrase for {url}: {phrase}")
        for phrase in contract["forbidden_phrases"]:
            if phrase in description:
                errors.append(f"forbidden README phrase for {url}: {phrase}")
    return tuple(errors)


class GithubAnchorTests(unittest.TestCase):
    def test_matches_github_heading_style(self) -> None:
        self.assertEqual(
            github_anchor("Official & League Data"), "official--league-data"
        )


class DocumentValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_directory.name)
        for filename in ("LICENSE", "code-of-conduct.md", "contributing.md"):
            (self.root / filename).touch()

    def tearDown(self) -> None:
        self.temp_directory.cleanup()

    def test_accepts_the_catalog_contract(self) -> None:
        result = validate_document(VALID_README, self.root)

        self.assertEqual(result.errors, ())
        self.assertEqual(result.resource_count, 1)
        self.assertEqual(result.contents_count, 1)

    def test_reports_contents_and_resource_format_errors(self) -> None:
        invalid = VALID_README.replace(
            "- [Official & League Data](#official--league-data)",
            "- [Contribute](#contribute)",
        ).replace(
            "- [Example](https://example.com/) - Example primary source.",
            "- [Example](http://example.com/) - lowercase description",
        )

        result = validate_document(invalid, self.root)

        self.assertTrue(
            any("Contents entries must match" in error for error in result.errors)
        )
        self.assertTrue(any("must use HTTPS" in error for error in result.errors))
        self.assertTrue(any("start uppercase" in error for error in result.errors))
        self.assertTrue(any("end with a period" in error for error in result.errors))

    def test_reports_malformed_and_duplicate_resources(self) -> None:
        invalid = VALID_README.replace(
            "- [Example](https://example.com/) - Example primary source.",
            "\n".join(
                (
                    "- [Example](https://example.com/) - Example primary source.",
                    "- [Duplicate](https://example.com/) - Duplicate canonical URL.",
                    "- [Malformed](https://malformed.example/) Description without separator.",
                )
            ),
        )

        result = validate_document(invalid, self.root)

        self.assertTrue(
            any("duplicate resource URL" in error for error in result.errors)
        )
        self.assertTrue(
            any("resource entry must match" in error for error in result.errors)
        )

    def test_reports_missing_relative_links(self) -> None:
        invalid = VALID_README + "\n[Missing](docs/missing.md)\n"

        result = validate_document(invalid, self.root)

        self.assertIn(
            "relative link for 'Missing' points to missing file: docs/missing.md",
            result.errors,
        )

    def test_reports_non_ascii_characters(self) -> None:
        invalid = VALID_README.replace("focused", f"foc{chr(0x016B)}sed")

        result = validate_document(invalid, self.root)

        self.assertIn(
            "line 3: document must use ASCII characters; found U+016B",
            result.errors,
        )

    def test_empty_document_reports_errors_instead_of_crashing(self) -> None:
        result = validate_document("", self.root)

        self.assertTrue(result.errors)
        self.assertEqual(result.resource_count, 0)


class RepositoryTextContractTests(unittest.TestCase):
    def test_publishable_text_files_are_ascii(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]

        for relative_path in PUBLISHABLE_TEXT_FILES:
            with self.subTest(path=relative_path):
                contents = (repository_root / relative_path).read_bytes()
                self.assertTrue(
                    contents.isascii(), f"{relative_path} must contain only ASCII"
                )


class ReleaseSourceContractTests(unittest.TestCase):
    def setUp(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        self.readme = (repository_root / "README.md").read_text(encoding="utf-8")

    def test_release_sources_match_reviewed_evidence(self) -> None:
        self.assertEqual(_release_source_contract_errors(self.readme), ())

    def test_release_source_contract_rejects_boundary_mutations(self) -> None:
        draft_mutation = self.readme.replace(
            "not a bulk-data license", "is a bulk-data license"
        )
        combine_mutation = self.readme.replace(
            "does not establish bulk retrieval or redistribution rights",
            "establishes bulk retrieval or redistribution rights",
        )

        draft_errors = _release_source_contract_errors(draft_mutation)
        combine_errors = _release_source_contract_errors(combine_mutation)

        self.assertTrue(
            any("forbidden README phrase" in error for error in draft_errors)
        )
        self.assertTrue(
            any("forbidden README phrase" in error for error in combine_errors)
        )


class LiveDataGuidanceTests(unittest.TestCase):
    """Offline editorial contracts, not live availability or source-quality checks.

    First-party evidence rechecked September 2, 2026 (a targeted agent check,
    not a human review of the whole catalog):
    - https://www.nfl.com/scores (including preseason week selectors)
    - https://www.nfl.com/stats/player-stats/ (player categories; STATS navigation)
    - https://nflfastr.com/#data-access (regular season and postseason files)
    - https://github.com/nflverse/nfldata/blob/master/DATASETS.md#games
      (schedule excludes preseason; the PBP release builder obtains game IDs
      through missing_raw_pbp(), which uses load_schedules())
    - https://github.com/nflverse/nflverse-pbp/blob/master/R/update_pbp.R
    - https://nflfastr.com/reference/missing_raw_pbp.html
    - https://nflreadr.nflverse.com/articles/nflverse_data_schedule.html
      (Injury Data and nflverse Participation Data sections)
    - https://www.nfl.com/injuries/ (weekly reporting surface)

    Recheck these sources before deliberately changing the pinned guidance.
    Whitespace may change; resource identity and factual clauses may not drift.
    """

    def setUp(self) -> None:
        self.root = Path(__file__).resolve().parents[1]
        self.readme = (self.root / "README.md").read_text(encoding="utf-8")

    def assert_scores_statistics_contract(self, text: str) -> None:
        entries = _catalog_entries_by_url(text)
        for url, name, description in (
            (
                "https://www.nfl.com/scores",
                "NFL Scores",
                "Official preseason and regular-season schedules, live game status, "
                "final scores, recaps, highlights, and replay links.",
            ),
            (
                "https://www.nfl.com/stats/player-stats/",
                "NFL Statistics",
                "Official player leaderboards, with team statistics and standings "
                "linked from the NFL's statistics navigation.",
            ),
        ):
            self.assertEqual(
                entries.get(url),
                (name, "Official & League Data", description),
                "Scores/Statistics source distinction",
            )

        rows = [
            tuple(cell.strip() for cell in line.strip("|").split("|"))
            for line in text.splitlines()
            if line.startswith("|")
        ]
        self.assertIn(
            (
                "Live preseason schedules/results",
                "NFL Scores",
                "Licensed Sportradar or SportsDataIO feed for production use",
            ),
            rows,
            "live preseason stack recommendation",
        )

    def assert_preseason_contract(self, text: str) -> None:
        normalized = " ".join(text.split())
        self.assertIn(
            "For live or preseason games, begin with NFL Scores or a licensed API.",
            normalized,
            "live/preseason starting point",
        )
        self.assertIn(
            "nflfastR's published play-by-play files contain regular-season and "
            "postseason games, not preseason.",
            normalized,
            "nflfastR preseason exclusion",
        )

    def assert_injury_contract(self, text: str) -> None:
        normalized = " ".join(text.split())
        for clause in (
            "Do not depend on nflverse participation or injury files for current "
            "in-season reporting.",
            "Participation data from 2023 onward is released only after the "
            "postseason, and the nflverse injury source currently stops after "
            "2024 with no replacement ETA.",
            "Use the official NFL injury reports for current weekly designations.",
        ):
            self.assertIn(clause, normalized, "nflverse injury availability boundary")
        self.assertEqual(
            _catalog_entries_by_url(text).get("https://www.nfl.com/injuries/"),
            (
                "NFL Injury Reports",
                "Official & League Data",
                "Official practice participation and game-status designations "
                "while weekly reporting windows are active.",
            ),
            "official injury reporting boundary",
        )

    def test_scores_and_statistics_have_distinct_roles(self) -> None:
        self.assert_scores_statistics_contract(self.readme)

    def test_published_pbp_excludes_preseason(self) -> None:
        self.assert_preseason_contract(self.readme)

    def test_injury_gap_and_weekly_alternative_are_explicit(self) -> None:
        self.assert_injury_contract(self.readme)

    def test_guidance_allows_prose_rewrapping(self) -> None:
        rewrapped = self.readme.replace("play-by-play files", "play-by-play\nfiles")
        rewrapped = rewrapped.replace("2024 with no", "2024\nwith no")
        self.assert_preseason_contract(rewrapped)
        self.assert_injury_contract(rewrapped)

    def test_rejects_scores_statistics_mutations(self) -> None:
        mutations = (
            ("[NFL Scores]", "[NFL Statistics]", "source distinction"),
            (
                "https://www.nfl.com/scores",
                "https://www.nfl.com/schedules",
                "source distinction",
            ),
            (
                "Official player leaderboards",
                "Official live scores",
                "source distinction",
            ),
            (
                "Official preseason and regular-season schedules",
                "Official regular-season schedules",
                "source distinction",
            ),
            ("| NFL Scores ", "| NFL Statistics ", "stack recommendation"),
        )
        for old, new, failure in mutations:
            with self.subTest(mutation=(old, new)):
                mutated = self.readme.replace(old, new, 1)
                self.assertNotEqual(mutated, self.readme)
                self.assertEqual(validate_document(mutated, self.root).errors, ())
                with self.assertRaisesRegex(AssertionError, failure):
                    self.assert_scores_statistics_contract(mutated)

    def test_rejects_preseason_guidance_mutations(self) -> None:
        mutations = (
            ("begin with NFL Scores", "begin with NFL Statistics", "starting point"),
            (
                "games, not preseason.",
                "games, including preseason.",
                "preseason exclusion",
            ),
            ("games, not preseason.", "games.", "preseason exclusion"),
            (
                "regular-season and postseason games",
                "regular-season games",
                "preseason exclusion",
            ),
        )
        for old, new, failure in mutations:
            with self.subTest(mutation=(old, new)):
                mutated = self.readme.replace(old, new, 1)
                self.assertNotEqual(mutated, self.readme)
                self.assertEqual(validate_document(mutated, self.root).errors, ())
                with self.assertRaisesRegex(AssertionError, failure):
                    self.assert_preseason_contract(mutated)

    def test_rejects_injury_guidance_mutations(self) -> None:
        mutations = (
            (
                "Do not depend on nflverse",
                "Depend on nflverse",
                "availability boundary",
            ),
            ("stops after 2024", "stops after 2025", "availability boundary"),
            (
                "with no replacement ETA",
                "with a replacement ETA",
                "availability boundary",
            ),
            (
                "released only after the postseason",
                "released during the season",
                "availability boundary",
            ),
            (
                "official NFL injury reports for",
                "nflverse injury files for",
                "availability boundary",
            ),
            (
                "while weekly reporting windows are active",
                "throughout the year",
                "reporting boundary",
            ),
        )
        for old, new, failure in mutations:
            with self.subTest(mutation=(old, new)):
                # Match across prose wrapping without flattening the Markdown.
                pattern = r"\s+".join(re.escape(word) for word in old.split())
                self.assertEqual(len(re.findall(pattern, self.readme)), 1)
                mutated = re.sub(pattern, new, self.readme, count=1)
                self.assertNotEqual(mutated, self.readme)
                self.assertEqual(validate_document(mutated, self.root).errors, ())
                with self.assertRaisesRegex(AssertionError, failure):
                    self.assert_injury_contract(mutated)


if __name__ == "__main__":
    unittest.main()
