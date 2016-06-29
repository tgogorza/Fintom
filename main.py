from Fintom.Reader import YahooReader
from Fintom.Reader import GoogleReader

reader = YahooReader()
reader.pull_historical_data('TSLA')
reader = GoogleReader()
reader.pull_historical_data('IBB')
