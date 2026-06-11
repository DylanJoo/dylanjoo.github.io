#!/usr/bin/env python3
"""Convert _data/publications.bib -> _data/publications.yml for Jekyll."""

import os
import re
import yaml
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB_PATH = os.path.join(ROOT, "_data", "publications.bib")
OUT_PATH = os.path.join(ROOT, "_data", "publications.yml")

ENTRYTYPE_TO_PUBTYPE = {
    "article": "journal",
    "inproceedings": "conference",
    "proceedings": "conference",
    "misc": "preprint",
    "techreport": "report",
    "unpublished": "preprint",
}


def strip_braces(text):
    return re.sub(r"[{}\\]", "", text or "").strip()


def parse_authors(author_str):
    """'Last, First and Last2, First2' -> ['First Last', 'First2 Last2']"""
    names = []
    for raw in re.split(r"\s+and\s+", (author_str or "").strip()):
        name = strip_braces(raw.strip())
        if "," in name:
            last, first = name.split(",", 1)
            name = f"{first.strip()} {last.strip()}"
        names.append(name)
    return names


def resolve_pubtype(entry):
    custom = strip_braces(entry.get("type", "")).lower()
    if custom in ("conference", "journal", "demo", "workshop", "preprint", "report"):
        return custom
    return ENTRYTYPE_TO_PUBTYPE.get(entry.get("ENTRYTYPE", "").lower(), "conference")


def main():
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    parser.ignore_nonstandard_types = False

    with open(BIB_PATH) as f:
        db = bibtexparser.load(f, parser=parser)

    publications = []
    for entry in db.entries:
        venue = strip_braces(entry.get("booktitle") or entry.get("journal") or "")
        pubtype = resolve_pubtype(entry)

        pub = {
            "id": entry["ID"],
            "title": strip_braces(entry.get("title", "")),
            "authors": parse_authors(entry.get("author", "")),
            "year": int(entry.get("year", 0)),
            "pubtype": pubtype,
            "abbr": strip_braces(entry.get("abbr", "")),
            "venue": venue,
            "abstract": (entry.get("abstract") or "").strip(),
            "award": strip_braces(entry.get("award", "")),
            "selected": strip_braces(entry.get("selected", "")).lower() in ("true", "yes", "1"),
            "equal": [
                a.strip()
                for a in strip_braces(entry.get("equal", "")).split(",")
                if a.strip()
            ],
        }

        links = {}
        for key in ("paper", "slides", "code", "poster", "demo", "video"):
            val = (entry.get(key) or "").strip()
            if val:
                links[key] = val
        if "url" in entry and entry["url"].strip() and "paper" not in links:
            links["paper"] = entry["url"].strip()
        pub["links"] = links

        publications.append(pub)

    # Sort by year desc; within a year: conference > journal > demo > workshop > preprint
    type_rank = {"conference": 0, "journal": 1, "demo": 2, "workshop": 3, "preprint": 4, "report": 5}
    publications.sort(key=lambda p: (-p["year"], type_rank.get(p["pubtype"], 9)))

    with open(OUT_PATH, "w") as f:
        yaml.dump(publications, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Wrote {len(publications)} publications to {OUT_PATH}")


if __name__ == "__main__":
    main()
