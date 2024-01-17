import unittest
import pandas as pd
from scripts.homework_c4 import (filter_genre,filter_year,filter_higher_mean)

df = pd.read_csv("FilmGenreStats.csv")

class TestFilteringFunctions(unittest.TestCase):
    def setUp(self):
        self.path = "datasets/FilmGenreStats.csv"
        pass

    def test_filter_genre(self):

        df = filter_genre("Action")
        self.assertTrue(all(df["Genre"] == "Action"))

    def test_filter_year(self):

        df = filter_year(2010)
        self.assertTrue(all(df["Year"] == 2010))

    def test_filter_higher_mean(self):

        df = filter_higher_mean()
        mean = df["Gross"].mean()
        self.assertTrue(all(df["Gross"] > mean))



if __name__ == '__main__':
    unittest.main()