# Exercise 2.6

import csv

with open('Data/prices.csv', 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)