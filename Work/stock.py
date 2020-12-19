class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, nshares):
        self.shares -= nshares

    def cost(self):
        costs = self.shares * self.price
        return costs