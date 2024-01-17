"""
Testing the functions
"""
import unittest
import pandas as pd
from scripts.homework import Filter_data


class TestFilterData(unittest.TestCase):
    """
    Class to test the functions
    """
    def setUp(self):
        """
        Creating own dataset
        """
        data = {
            "Genre": ["Action", "Comedy", "Drama", "Action"],
            "Year": [2010, 2010, 2015, 2015],
            "Gross": [100, 200, 150, 300],
        }
        self.df = pd.DataFrame(data)
        self.filter_data = Filter_data(self.df)

    def test_filter_genre(self):
        """
        Test for filter genre
        """
        result = self.filter_data.filter_genre("Action")
        expected = self.df[self.df["Genre"] == "Action"]
        pd.testing.assert_frame_equal(result, expected)

    def test_filter_year(self):
        """
        Testing filter year
        """
        result = self.filter_data.filter_year(2015)
        expected = self.df[self.df["Year"] == 2015]
        pd.testing.assert_frame_equal(result, expected)

    def test_filter_higher_mean(self):
        """
        Testing higher mean filter
        """
        result = self.filter_data.filter_higher_mean()
        mean = self.df["Gross"].mean()
        expected = self.df[self.df["Gross"] > mean]
        pd.testing.assert_frame_equal(result, expected)


if __name__ == "__main__":
    unittest.main()
