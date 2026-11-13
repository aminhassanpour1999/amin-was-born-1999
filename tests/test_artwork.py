import unittest
import a_m_in_was_born as artwork


class ArtworkTests(unittest.TestCase):
    def test_phrase_is_exact(self):
        self.assertEqual(artwork.PHRASE, "AMIN WAS BORN")

    def test_font_contains_every_letter(self):
        self.assertEqual(set(artwork.FONT), set("AMINWSBOR"))

    def test_canvas_is_seven_by_fifty_two(self):
        grid = artwork.canvas()
        self.assertEqual(len(grid), 7)
        self.assertTrue(all(len(row) == 52 for row in grid))

    def test_first_and_last_rows_are_empty(self):
        grid = artwork.canvas()
        self.assertEqual(grid[0], "." * 52)
        self.assertEqual(grid[6], "." * 52)

    def test_only_five_middle_rows_contain_art(self):
        grid = artwork.canvas()
        self.assertTrue(all("#" in row for row in grid[1:6]))

    def test_every_pixel_has_a_unique_1999_weekday(self):
        dates = [item[2] for item in artwork.pixel_dates()]
        self.assertEqual(len(dates), len(set(dates)))
        self.assertTrue(all(d.year == 1999 and d.weekday() < 5 for d in dates))

    def test_artwork_width_and_centering(self):
        rows = artwork.artwork_rows()
        self.assertTrue(all(len(row) == 51 for row in rows))
        grid = artwork.canvas()
        self.assertEqual(grid[1][0], "#")
        self.assertEqual(grid[1][-1], ".")

    def test_pixel_count(self):
        self.assertEqual(len(artwork.pixel_dates()), 121)


if __name__ == "__main__":
    unittest.main()
