import urllib
import os


class Reader(object):
    """Data reader"""

    def __init__(self):
        self.base_url = ''
        self.output_path = os.getcwd()

    def make_url(self, ticker_symbol):
        pass

    def make_filename(self, ticker_symbol, directory="Data"):
        return self.output_path + "/" + directory + "/" + ticker_symbol + ".csv"

    def pull_historical_data(self, ticker_symbol, directory="Data"):
        try:
            urllib.urlretrieve(self.make_url(ticker_symbol), self.make_filename(ticker_symbol, directory))
        except urllib.ContentTooShortError as e:
            outfile = open(self.make_filename(ticker_symbol, directory), "w")
            outfile.write(e.content)
            outfile.close()


class YahooReader(Reader):
    """" Reads historical data from Yahoo Finance """

    def __init__(self):
        super(YahooReader, self).__init__()
        self.base_url = "http://ichart.finance.yahoo.com/table.csv?s="

    def make_url(self, ticker_symbol):
        return self.base_url + ticker_symbol

    # def get_symbols(self, symbols, start_date = None, end_date = None):
    #     symbols = []
    #     for sym in symbols:
    #         hist_data = Share(sym)
    #         if hist_data:
    #             symbols.append()


class GoogleReader(Reader):
    """Reads historical data from Google Finance"""

    def __init__(self):
        super(GoogleReader, self).__init__()
        self.base_url = "http://www.google.com/finance/historical?q={0}&output=csv"

    def make_url(self, ticker_symbol):
        return self.base_url.format(ticker_symbol)

    # def getSymbols(self, symbols, startDate, endDate):
