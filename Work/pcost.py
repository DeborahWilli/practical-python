# pcost.py
import csv
import sys


def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row_no, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f"Row {row_no}: Could not convert: {row}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)