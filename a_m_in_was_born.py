#!/usr/bin/env python3
"""Draw AMIN WAS BORN on the 1999 GitHub contribution graph."""

from __future__ import annotations

import argparse
import subprocess
from datetime import date, datetime, time, timedelta, timezone

CANVAS_WEEKS = 52
TEST_MARKER = "[AMIN-WAS-BORN-1999-TEST]"
FULL_MARKER = "[AMIN-WAS-BORN-1999-FULL]"
PHRASE = "AMIN WAS BORN"

FONT = {
    "A": ("010", "101", "111", "101", "101"),
    "M": ("10001", "11011", "10101", "10001", "10001"),
    "I": ("111", "010", "010", "010", "111"),
    "N": ("1001", "1101", "1011", "1001", "1001"),
    "W": ("10001", "10001", "10101", "10101", "01010"),
    "S": ("111", "100", "111", "001", "111"),
    "B": ("110", "101", "110", "101", "110"),
    "O": ("111", "101", "101", "101", "111"),
    "R": ("110", "101", "110", "101", "101"),
}


def artwork_rows() -> list[str]:
    """Render the five-line bitmap phrase with a two-column word gap."""
    words = PHRASE.split()
    rendered_words = []
    for word in words:
        rendered_words.append([
            " ".join(FONT[letter][row] for letter in word)
            for row in range(5)
        ])
    return [
        "  ".join(word_rows[row] for word_rows in rendered_words)
        for row in range(5)
    ]


def canvas() -> list[str]:
    """Return a centered 7×52 contribution grid; Sunday/Saturday stay blank."""
    rows = ["." * CANVAS_WEEKS]
    for line in artwork_rows():
        if len(line) > CANVAS_WEEKS:
            raise ValueError("Artwork is wider than the 52-week canvas")
        left = (CANVAS_WEEKS - len(line)) // 2
        rows.append("." * left + line.replace("0", ".").replace("1", "#")
                    + "." * (CANVAS_WEEKS - left - len(line)))
    rows.append("." * CANVAS_WEEKS)
    return rows


def pixel_dates() -> list[tuple[int, int, date]]:
    """Map each lit pixel to a unique Monday–Friday date in 1999."""
    grid = canvas()
    first_monday = date(1999, 1, 4)
    result = []
    for day_index in range(1, 6):
        for week_index, cell in enumerate(grid[day_index]):
            if cell == "#":
                result.append((
                    week_index,
                    day_index,
                    first_monday + timedelta(weeks=week_index, days=day_index - 1),
                ))
    return result


def marker_exists(marker: str) -> bool:
    result = subprocess.run(
        ["git", "log", "--all", "--fixed-strings", f"--grep={marker}"],
        check=True, capture_output=True, text=True,
    )
    return bool(result.stdout.strip())


def git_empty_commit(message: str, commit_date: date, email: str) -> None:
    stamp = datetime.combine(commit_date, time(12, 0), tzinfo=timezone.utc)
    iso = stamp.isoformat()
    env = {
        "GIT_AUTHOR_NAME": "Amin Hassanpour",
        "GIT_AUTHOR_EMAIL": email,
        "GIT_COMMITTER_NAME": "Amin Hassanpour",
        "GIT_COMMITTER_EMAIL": email,
        "GIT_AUTHOR_DATE": iso,
        "GIT_COMMITTER_DATE": iso,
    }
    import os
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", message],
        check=True, env={**os.environ, **env},
    )


def run(mode: str, email: str) -> None:
    if not email or "@" not in email:
        raise ValueError("Provide an email address verified on your GitHub account.")
    if mode == "test":
        if marker_exists(TEST_MARKER):
            raise SystemExit("The TEST commit already exists; refusing to duplicate it.")
        test_date = pixel_dates()[0][2]
        git_empty_commit(f"{TEST_MARKER} Verify historical attribution", test_date, email)
        print(f"Created one TEST commit dated {test_date.isoformat()}.")
        return

    if not marker_exists(TEST_MARKER):
        raise SystemExit("Run and verify TEST before FULL.")
    if marker_exists(FULL_MARKER):
        raise SystemExit("FULL artwork already exists; refusing to duplicate it.")

    pixels = pixel_dates()
    for index, (x, y, pixel_date) in enumerate(pixels, start=1):
        git_empty_commit(
            f"{FULL_MARKER} pixel {index:03d}/{len(pixels)} at week {x + 1}, weekday {y}",
            pixel_date, email,
        )
    print(f"Created exactly {len(pixels)} artwork commits.")


def main() -> None:
    parser = argparse.ArgumentParser(description=PHRASE)
    parser.add_argument("--mode", choices=("test", "full", "preview"), default="preview")
    parser.add_argument("--email", default="")
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args()
    if args.preview or args.mode == "preview":
        for row in canvas():
            print(row)
        print(f"Pixels: {len(pixel_dates())}")
        return
    run(args.mode, args.email)


if __name__ == "__main__":
    main()
