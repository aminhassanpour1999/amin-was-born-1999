# AMIN WAS BORN — 1999

A small piece of personal pixel art drawn on the GitHub contribution graph using empty commits dated in 1999.

**Artwork:** `AMIN WAS BORN`  
**Year:** 1999  
**Pixels / artwork commits:** 121  
**Canvas:** 52 weeks × 7 days. The first and last rows are intentionally empty; the lettering occupies Monday–Friday.

## Preview

```text
....................................................
.#. #...# ### #..#  #...# .#. ###  ##. ### ##. #..#.
#.# ##.## .#. ##.#  #...# #.# #..  #.# #.# #.# ##.#.
### #.#.# .#. #.##  #.#.# ### ###  ##. #.# ##. #.##.
#.# #...# .#. #..#  #.#.# #.# ..#  #.# #.# #.# #..#.
#.# #...# ### #..#  .#.#. #.# ###  ##. ### #.# #..#.
....................................................
```

The preview is generated from the same bitmap font used by the script. The complete phrase is **AMIN WAS BORN**; no letter is abbreviated or omitted.

## Safe, two-stage workflow

1. Open **Actions → Draw 1999 artwork**.
2. Run with `mode=TEST`, `confirmation=YES`, and an email address verified on your GitHub account.
3. Confirm the single test commit appears in the 1999 contribution graph.
4. Only after that confirmation, run again with `mode=FULL` and `confirmation=YES`.

The full run creates exactly one empty commit per lit pixel. It does not rewrite history or force-push.

## Local checks

```bash
python3 -m unittest discover -s tests -v
python3 a_m_in_was_born.py --preview
```

## Important

GitHub contribution visibility depends on commit attribution and GitHub's contribution rules. The TEST run exists to verify visibility before creating the full artwork.
