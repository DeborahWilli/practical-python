import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    types = [str, int, float]

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {name: func(val) for name, func, val in zip(headers, types, row)}
            portfolio.append(stock)

    return portfolio


portfolio = read_portfolio("Data/portfolio.csv")