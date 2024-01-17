"""
Script to make test on functions
"""
import unittest
import pandas as pd
import click

df = pd.read_csv("FilmGenreStats.csv")

@click.command(short_help="parser to import dataset")
@click.option("-g", "--genre", required=True, help="Genre to filter")
@click.option("-y", "--year", required=True, help="Year to filter")


def filter_genre(genre):
        """
        filter by genre
        """
        return df[df["Genre"]== genre]

def filter_year(year):
        """
        Filter by year
        """
        return df[df["Year"]== year]

def filter_higher_mean():
        """
        Filter by higher revenue than mean
        """
        mean = df["Gross"].mean()
        return df[df["Gross"]>mean]

print(df.head())

if __name__ == '__main__':
    unittest.main()