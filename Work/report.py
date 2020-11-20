# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
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
    report = []
    for pf in portfolio:
        stock = (pf["name"], pf["shares"], prices[pf["name"]], (prices[pf["name"]]-pf["price"]))
        report.append(stock)
    return report

# for r in report:
#         print(r)

# ('AA', 100, 9.22, -22.980000000000004)
# ('IBM', 50, 106.28, 15.180000000000007)
# ('CAT', 150, 35.46, -47.98)
# ('MSFT', 200, 20.89, -30.339999999999996)
# ('GE', 95, 13.48, -26.889999999999997)

# Calling the functions
portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)


# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s["shares"] * s["price"]
#print("Total cost:", total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s["shares"] * prices[s["name"]]
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