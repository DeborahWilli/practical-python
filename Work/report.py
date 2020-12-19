# report.py
#
# Exercise 2.4

import csv
import sys
import stock
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


def print_report(report):
    """
    Print the formatted output of the report
    """
    headers = ("Name", "Shares", "Price", "Change")
    print('{name:>10s} {shares:>10s} {price:>10s} {change:>10s}'.format(
        name=headers[0], shares=headers[1], price=headers[2], change=headers[3]))
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        price = "${:.2f}".format(r[2])
        print('{:>10s} {:>10d} {:>10s} {:>10.2f}'.format(r[0], r[1], price, r[3]))

def portfolio_report(portfolio_filename, prices_filename):
    """
    Read in the desired portfolio and prices data, create a report afterwards and 
    eventually print the report.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    # Calling the functions
    portfolio_report(args[1], args[2])

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
