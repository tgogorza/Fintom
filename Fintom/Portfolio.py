class Portfolio:

    '''
    Portfolio with stocks
    '''

    def __init__(self):
        self.symbols = []
        self.cum_ret = 0
        self.sharpe = 0

    def add_symbol(self, stock):
        self.symbols.append(stock)

