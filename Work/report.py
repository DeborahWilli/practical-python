# report.py
#
# Exercise 2.4

import csv
import sys
import stock
import tableformat
from pprint import pprint
from fileparse import parse_csv

# Once you have done that, fix all of the code in report.py and pcost.py so that it works with 
# Stock instances instead of dictionaries.

# Hint: You should not have to make major changes to the code. 
# You will mainly be changing dictionary access such as s['shares'] into s.shares.

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        pf_dict = parse_csv(file, select=["name", "shares", "price"], types=[str, int, float])
        portfolio = [stock.Stock(pf['name'], pf['shares'], pf['price']) for pf in pf_dict]
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as file:
        prices = dict(parse_csv(file, types=[str, float], has_headers=False))
    return prices


def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for pf in portfolio:
        current_price = prices[pf.name]
        change = current_price - pf.price
        summary = (pf.name, pf.shares, current_price, change)
        report.append(summary)
    return report


def print_report(reportdata, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    main(sys.argv)


# Calculate the total cost of the portfolio
#total_cost = 0.0
#for s in portfolio:
#    total_cost += s["shares"] * s["price"]
#print("Total cost:", total_cost)

# Compute the current value of the portfolio
#total_value = 0.0
#for s in portfolio:
#    total_value += s["shares"] * prices[s["name"]]
#print("Current value:", total_value)
#print("Gain:", total_value - total_cost)
