# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name': record['name'],
                 'shares': int(record['shares']),
                 'price': float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for pf in portfolio:
        current_price = prices[pf["name"]]
        change = current_price - pf["price"]
        summary = (pf["name"], pf["shares"], current_price, change)
        report.append(summary)
    return report


# Calling the functions
portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)


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

# Print the formatted reports
headers = ("Name", "Shares", "Price", "Change")
print('{name:>10s} {shares:>10s} {price:>10s} {change:>10s}'.format(
    name=headers[0], 
    shares=headers[1], 
    price=headers[2], 
    change=headers[3]))
print(('-' * 10 + ' ') * len(headers))
for r in report:
    price = "${:.2f}".format(r[2])
    print('{:>10s} {:>10d} {:>10s} {:>10.2f}'.format(r[0], r[1], price, r[3]))