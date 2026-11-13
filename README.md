# AMIN WAS BORN — 1999

A personal pixel-art tribute drawn on the GitHub contribution graph with empty Git commits dated in 1999.

**Artwork:** `AMIN WAS BORN`  
**Year:** 1999  
**Artwork pixels:** 121  
**Artwork commits:** 121  
**Canvas:** 52 weeks × 7 days. The first and last rows are intentionally empty; the lettering occupies Monday–Friday.

## Preview

```text
....................................................
.#..#...#.###.#..#..#...#..#..###..##..###.##..#..#.
#.#.##.##..#..##.#..#...#.#.#.#....#.#.#.#.#.#.##.#.
###.#.#.#..#..#.##..#.#.#.###.###..##..#.#.##..#.##.
#.#.#...#..#..#..#..#.#.#.#.#...#..#.#.#.#.#.#.#..#.
#.#.#...#.###.#..#...#.#..#.#.###..##..###.#.#.#..#.
....................................................
```

The preview is generated from the same bitmap font used by the script. The complete phrase is **AMIN WAS BORN**.

## Project status

## Completed artwork
The complete artwork has already been generated and pushed to the `main` branch. The 121 artwork commits are numbered `001/121` through `121/121`, use unique dates in 1999, and share the same repository tree (they do not modify project files).

A separate TEST commit was created on the date of the first artwork pixel to verify contribution attribution. It overlaps that pixel's date and is not an additional artwork pixel.

**Do not run the FULL workflow again on this completed history.** The script includes a duplicate-run guard and will refuse to generate the artwork a second time.

## Repository structure

- `a_m_in_was_born.py` — bitmap font, layout, date mapping, preview, and commit generation.
- `tests/test_artwork.py` — automated checks for the artwork geometry and pixel data.
- `docs/DESIGN.md` — design and layout decisions.
- `.github/workflows/draw-1999.yml` — manual GitHub Actions workflow for validation and controlled generation.

## Local validation

Python 3.12 or newer is recommended. No third-party packages are required.

Run the test suite:

```bash
python3 -m unittest discover -s tests -v
```

Render the artwork preview without creating commits:

```bash
python3 a_m_in_was_born.py --preview
```

## Historical contribution notes

GitHub's contribution graph applies its own attribution and display rules. Commits are authored with the account's verified email address and placed on the default branch. The one-pixel TEST run was used to verify that the historical year is attributed correctly before the full generation.

The generated commits intentionally have no file changes: the contribution graph is the artwork.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
