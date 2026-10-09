"""Regression checks for the topic catalog; no network or third-party packages."""
from collections import Counter
from contextlib import contextmanager, redirect_stdout
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog", ROOT / "scripts/catalog.py")
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)

RESERVED_ANCHORS = (
    "scope", "at-a-glance", "how-to-use", "browse-by-topic", "paper-index",
    "evidence-and-scope", "known-gaps", "maintenance", "reading-routes",
)
PAPER_COLUMNS = ["年份 / 来源", "论文", "为什么读", "研究定位"]
ORIGINAL_ROUTES = (
    ("fortunato-2018-science-of-science", "gopal-2025-inventing-with-machines",
     "wang-2023-scientific-discovery-ai", "messeri-2024-illusions-understanding",
     "hao-2026-ai-impact-science-focus"),
    ("kobak-2025-llm-excess-vocabulary", "liang-2025-quantifying-llm-scientific-papers",
     "kusumegi-2025-scientific-production-llms", "renault-2026-llm-production-timing-bias",
     "qian-2026-llm-us-research-funding", "tang-2025-gender-disparities-generative-ai"),
    ("uzzi-2013-atypical-combinations", "park-2023-less-disruptive",
     "petersen-2024-disruption-citation-inflation", "de-freitas-2025-ideation-generative-ai",
     "sourati-2023-human-aware-ai", "bianchini-2022-ai-emerging-method-invention",
     "bianchini-2026-ai-science-when-where"),
    ("liang-2024-monitoring-ai-peer-reviews", "thakkar-2026-randomized-peer-review-feedback",
     "kapoor-2023-leakage", "ahmed-2023-industry-ai", "lu-2026-end-to-end-ai-research",
     "tang-2025-risks-ai-scientists"),
    ("ding-2010-it-scientists-productivity", "hager-2024-measuring-science",
     "hill-2025-scooped-priority", "hill-2025-race-to-bottom", "azoulay-2019-funeral-science"),
)


class CatalogTestCase(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
        self.log = json.loads((ROOT / "data/search-log.json").read_text(encoding="utf-8"))

    def outputs(self):
        self.assertTrue(callable(getattr(catalog, "render_outputs", None)),
                        "The renderer must produce README, routes, and topic pages")
        return catalog.render_outputs(self.data, self.log)

    @contextmanager
    def temporary_catalog(self):
        """Use real generated files and manual documentation in an isolated root."""
        with tempfile.TemporaryDirectory(prefix="sos-catalog-test-") as directory:
            root = Path(directory).resolve()
            (root / "data").mkdir()
            (root / "data/papers.json").write_text(
                json.dumps(self.data, ensure_ascii=False), encoding="utf-8")
            (root / "data/search-log.json").write_text(
                json.dumps(self.log, ensure_ascii=False), encoding="utf-8")
            shutil.copy2(ROOT / "CONTRIBUTING.md", root / "CONTRIBUTING.md")
            outputs = self.outputs()
            for source in (ROOT / "docs").rglob("*.md"):
                relative = source.relative_to(ROOT)
                if relative.as_posix() not in outputs:
                    destination = root / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, destination)
            for relative, contents in outputs.items():
                destination = root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(contents, encoding="utf-8")
            with patch.object(catalog, "ROOT", root):
                yield root

    def run_check(self):
        with patch.object(sys, "argv", ["catalog.py", "--check"]), redirect_stdout(io.StringIO()):
            catalog.main()


class TopicValidationTests(CatalogTestCase):
    def test_current_catalog_is_a_complete_six_topic_partition(self):
        papers = catalog.validate(self.data, self.log)
        self.assertEqual(len(papers), 40)
        self.assertEqual(len(self.data["topic_sections"]), 6)
        assigned = [pid for topic in self.data["topic_sections"] for pid in topic["paper_ids"]]
        self.assertEqual(Counter(assigned), Counter(p["id"] for p in papers))

    def test_rejects_a_paper_assigned_to_two_topics(self):
        topics = self.data["topic_sections"]
        topics[1]["paper_ids"].append(topics[0]["paper_ids"][0])
        with self.assertRaises(ValueError):
            catalog.validate(self.data, self.log)

    def test_rejects_missing_papers_or_missing_topics(self):
        original = deepcopy(self.data)
        for remove_all in (False, True):
            with self.subTest(remove_all=remove_all):
                self.data = deepcopy(original)
                if remove_all:
                    self.data["topic_sections"] = []
                else:
                    self.data["topic_sections"][0]["paper_ids"].pop()
                with self.assertRaises(ValueError):
                    catalog.validate(self.data, self.log)

    def test_rejects_unknown_and_repeated_paper_references(self):
        original = deepcopy(self.data)
        for reference in ("unknown-paper", self.data["topic_sections"][0]["paper_ids"][0]):
            with self.subTest(reference=reference):
                self.data = deepcopy(original)
                self.data["topic_sections"][0]["paper_ids"].append(reference)
                with self.assertRaises(ValueError):
                    catalog.validate(self.data, self.log)

    def test_rejects_topic_ids_that_collide_with_existing_anchors(self):
        original = deepcopy(self.data)
        conflicts = (*RESERVED_ANCHORS, self.data["papers"][0]["id"],
                     self.data["topic_sections"][1]["id"])
        for conflict in conflicts:
            with self.subTest(anchor=conflict):
                self.data = deepcopy(original)
                self.data["topic_sections"][0]["id"] = conflict
                with self.assertRaises(ValueError):
                    catalog.validate(self.data, self.log)


class TopicRenderingTests(CatalogTestCase):
    def test_renders_all_eight_outputs_without_changing_paper_records(self):
        original = deepcopy(self.data)
        outputs = self.outputs()
        expected = {"README.md", "docs/reading-routes.md"}
        expected.update(f"topics/{topic['id']}.md" for topic in self.data["topic_sections"])
        self.assertEqual(set(outputs), expected)
        self.assertEqual(len(outputs), 8)
        self.assertEqual(catalog.render(self.data, self.log), outputs["README.md"])
        self.assertEqual(self.data, original)

    def test_each_paper_has_one_canonical_detail_and_a_compatible_readme_anchor(self):
        outputs = self.outputs()
        readme = outputs["README.md"]
        topic_texts = {name: text for name, text in outputs.items() if name.startswith("topics/")}
        for topic in self.data["topic_sections"]:
            self.assertIn(f'<a id="{topic["id"]}"></a>', readme)
            canonical = f"topics/{topic['id']}.md"
            for pid in topic["paper_ids"]:
                with self.subTest(paper=pid):
                    anchor = f'<a id="{pid}"></a>'
                    self.assertEqual(sum(text.count(anchor) for text in topic_texts.values()), 1)
                    self.assertIn(anchor, outputs[canonical])
                    self.assertEqual(readme.count(anchor), 1)
                    row = next(line for line in readme.splitlines() if anchor in line)
                    self.assertTrue(row.startswith("|"), "Legacy anchors belong to index rows")
                    self.assertIn(f"({canonical}#{pid})", row)
                    paper = next(p for p in self.data["papers"] if p["id"] == pid)
                    self.assertIn(paper["summary_zh"], outputs[canonical])
                    self.assertIn(paper["limitations_zh"], outputs[canonical])
        self.assertIn('<a id="scientific-literature"></a>', readme)

    def test_reading_routes_preserve_order_and_link_to_canonical_details(self):
        text = self.outputs()["docs/reading-routes.md"]
        topic_by_paper = {pid: topic["id"] for topic in self.data["topic_sections"]
                          for pid in topic["paper_ids"]}
        self.assertEqual(tuple(tuple(route["paper_ids"]) for route in self.data["reading_routes"][:5]),
                         ORIGINAL_ROUTES)
        for route in self.data["reading_routes"]:
            with self.subTest(route=route["title"]):
                heading = re.search(r"^#{2,3} " + re.escape(route["title"]) + r"$", text, re.M)
                self.assertIsNotNone(heading, "Every route needs its own readable section")
                rest = text[heading.end():]
                next_heading = re.search(r"^#{1,3} ", rest, re.M)
                body = rest[:next_heading.start()] if next_heading else rest
                destinations = re.findall(r"^\d+\. \[[^\]]+\]\(([^)]+)\)", body, re.M)
                expected = [f"../topics/{topic_by_paper[pid]}.md#{pid}" for pid in route["paper_ids"]]
                self.assertEqual(destinations, expected)

    def test_paper_tables_share_four_columns_and_escape_embedded_pipes(self):
        self.data["papers"][0]["relevance_zh"] = "第一种解释 | 第二种解释"
        outputs = self.outputs()
        table_sizes = []
        for name, text in outputs.items():
            if name == "docs/reading-routes.md":
                continue
            for table in re.findall(r"(?:^\|.*\|\n)+", text, re.M):
                rows = table.strip().splitlines()
                columns = [cell.strip() for cell in re.split(r"(?<!\\)\|", rows[0])[1:-1]]
                if "论文" not in columns:
                    continue
                table_sizes.append(len(rows) - 2)
                with self.subTest(page=name):
                    self.assertEqual(columns, PAPER_COLUMNS)
                    for row in rows[1:]:
                        self.assertEqual(len(re.split(r"(?<!\\)\|", row)[1:-1]), 4, row)
        self.assertEqual(table_sizes, [len(topic["paper_ids"]) for topic in self.data["topic_sections"]],
                         "Each topic needs a complete table using the same columns")


class GeneratedFileTests(CatalogTestCase):
    def test_check_accepts_a_complete_current_catalog_without_writing(self):
        with self.temporary_catalog() as root:
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            self.run_check()
            after = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            self.assertEqual(after, before)

    def test_check_rejects_stale_and_missing_topic_pages(self):
        for change in ("stale", "missing"):
            with self.subTest(change=change), self.temporary_catalog() as root:
                target = root / "topics" / (self.data["topic_sections"][0]["id"] + ".md")
                if change == "stale":
                    target.write_text(target.read_text(encoding="utf-8") + "\n过期内容\n", encoding="utf-8")
                else:
                    target.unlink()
                with self.assertRaises((ValueError, OSError)):
                    self.run_check()

    def test_check_rejects_stale_reading_routes(self):
        with self.temporary_catalog() as root:
            (root / "docs/reading-routes.md").write_text("旧版阅读路线\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                self.run_check()

    def test_local_link_checker_inspects_topic_pages_and_target_anchors(self):
        for target in ("../docs/nonexistent.md", "../README.md#missing-paper-anchor"):
            with self.subTest(target=target), self.temporary_catalog() as root:
                catalog.check_local_links()
                page = root / "topics" / (self.data["topic_sections"][0]["id"] + ".md")
                with page.open("a", encoding="utf-8") as stream:
                    stream.write(f"\n[broken]({target})\n")
                with self.assertRaises(ValueError):
                    catalog.check_local_links()


if __name__ == "__main__":
    unittest.main()
