"""Refresh the live numbers in README.md from public APIs. Standard library only.

Rewrites the block between <!-- stats:start --> and <!-- stats:end -->.
If any source fails, the README is left untouched so a flaky API never
publishes a wrong number.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"
USER = "Gjusev"
PYPI_PACKAGES = ["voice-evals", "locale-invoice-check", "nitelos", "vision-input-check"]
BENCHMARK_DATASET = "Gjusev/voxentity-eu"


def get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "gjusev-profile-stats"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def pypi_downloads(package: str) -> int:
    data = get(f"https://pypistats.org/api/packages/{package}/overall?mirrors=false")["data"]
    return sum(row["downloads"] for row in data)


def hf_likes() -> tuple[int, int]:
    likes = repos = 0
    for kind in ("models", "datasets", "spaces"):
        for repo in get(f"https://huggingface.co/api/{kind}?author={USER}&limit=200&expand[]=likes"):
            likes += repo.get("likes", 0)
            repos += 1
    return likes, repos


def hf_dataset_downloads(repo_id: str) -> int:
    return get(f"https://huggingface.co/api/datasets/{repo_id}?expand[]=downloadsAllTime")["downloadsAllTime"]


def fmt(n: int) -> str:
    return f"{n:,}"


def main() -> int:
    try:
        pypi = sum(pypi_downloads(p) for p in PYPI_PACKAGES)
        likes, hf_repos = hf_likes()
        bench = hf_dataset_downloads(BENCHMARK_DATASET)
    except Exception as exc:  # noqa: BLE001 - any failure keeps the old numbers
        print(f"stats fetch failed, README unchanged: {exc}", file=sys.stderr)
        return 0

    today = dt.date.today().isoformat()
    cells = [
        ("3", "products<br>in production"),
        (fmt(pypi), f"PyPI downloads<br>{len(PYPI_PACKAGES)} packages"),
        (fmt(bench), "downloads of the<br>VoxEntity-EU benchmark"),
        (fmt(likes), f"likes on Hugging Face<br>{hf_repos} models, datasets, demos"),
    ]
    block = "\n".join([
        "<!-- stats:start -->",
        "<table><tr>",
        *(f'<td align="center" width="200"><h3>{n}</h3><sub>{label}</sub></td>' for n, label in cells),
        "</tr></table>",
        f"<sub>Live from PyPI and Hugging Face, checked daily · last change {today}</sub>",
        "<!-- stats:end -->",
    ])
    text = README.read_text(encoding="utf-8")
    new = re.sub(r"<!-- stats:start -->.*?<!-- stats:end -->", block, text, flags=re.S)
    undated = lambda s: re.sub(r" · \d{4}-\d{2}-\d{2}</sub>", "</sub>", s)  # noqa: E731
    # Only the numbers count as a change; a new date alone would mean a daily no-op commit.
    if undated(new) != undated(text):
        README.write_text(new, encoding="utf-8", newline="\n")
        print("README stats updated")
    else:
        print("README stats unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
