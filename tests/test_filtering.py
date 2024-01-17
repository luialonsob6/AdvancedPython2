"""
Test for Filtering functions
"""
import unittest
from scripts.homework import filter_genre, filter_year, filter_higher_mean

class TestFilteringFunctions(unittest.TestCase):
    """
    Class to test the filtering functions
    """
    def setUp(self):
        self.path = "scripts/FilmGenreStats.csv"

    def test_filter_genre(self):
        """
        Filtering by genre
        """
        df = filter_genre("Action")
        self.assertTrue(all(df["Genre"] == "Action"))

    def test_filter_year(self):
        """
        Filtering by year
        """
        df = filter_year(2010)
        self.assertTrue(all(df["Year"] == 2010))

    def test_filter_higher_mean(self):
        """
        Filtering by gross higher than mean.
        """
        df = filter_higher_mean()
        mean = df["Gross"].mean()
        self.assertTrue(all(df["Gross"] > mean))


if __name__ == "__main__":
    unittest.main()