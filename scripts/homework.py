"""
Script to make test on functions
"""
import unittest
import pandas as pd
import click


class Filterdata:
    """
    Define class with filter functions
    """

    def __init__(self, df):
        self.df = df

    def filter_genre(self, genre):
        """
        filter by genre
        """
        return self.df[self.df["Genre"] == genre]

    def filter_year(self, year):
        """
        Filter by year
        """
        return self.df[self.df["Year"] == year]

    def filter_higher_mean(self):
        """
        Filter by higher revenue than mean
        """
        mean = self.df["Gross"].mean()
        return self.df[self.df["Gross"] > mean]


@click.command(short_help="parser to import dataset")
@click.option("-i", "--insert", required=True, help="Path to my Input Dataset")
@click.option("-f", "--filtering", is_flag=True, help="Set a filtering or not")
@click.option("-g", "--genre", required=True, help="Genre to filter")
@click.option("-y", "--year", required=True, help="Year to filter")
def main(insert, filtering, genre, year):
    """
    Start functions
    """

    df = pd.read_csv(insert)

    print(df.shape)
    print(df.info())

    if filtering:
        print("Im going to filter")
        df = Filterdata(df).filter_genre(genre)
        df = Filterdata(df).filter_year(year)
        df = Filterdata(df).filter_higher_mean()
        print(df.shape)
        print(df.head())


if __name__ == "__main__":
    unittest.main()
