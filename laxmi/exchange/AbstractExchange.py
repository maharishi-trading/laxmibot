import logging
from abc import ABCMeta, abstractmethod


class AbstractExchange(metaclass=ABCMeta):


    def __init__(self):
        self.exchange = None

    @abstractmethod
    def create_market_buy_order(self, symbol, amount):
        pass

    @abstractmethod
    def create_market_sell_order(self, symbol, amount):
        pass

    def fetch_ticker(self, symbol):
        try:
            # Fetch real ticker data from the exchange
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker
        except Exception as e:
            logging.error(f"Error fetching ticker: {e}")
            return None


    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None):
        try:
            # Fetch real OHLCV data from the exchange
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, since, limit)
            return ohlcv
        except Exception as e:
            logging.error(f"Error fetching OHLCV: {e}")
            return None