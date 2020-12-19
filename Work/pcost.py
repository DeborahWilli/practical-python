# pcost.py
import csv
import sys

from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total_cost = sum([s.shares * s.price for s in portfolio])
    return total_cost

def main(args):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"
    cost = portfolio_cost(filename)
    print("Total cost:", cost)

if __name__ == "__main__":
    main(sys.argv)