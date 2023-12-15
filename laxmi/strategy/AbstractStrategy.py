import logging
from abc import ABCMeta, abstractmethod
from typing import Dict

from laxmi.exchange import AbstractExchange

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AbstractStrategy(metaclass=ABCMeta):
    def __init__(self, exchanges):
        self.exchanges: Dict[str, AbstractExchange] = exchanges

    @abstractmethod
    def execute(self):
        pass

    def fetch_price(self, symbol):
        prices = {}
        for exchange_id, exchange in self.exchanges.items():
            try:
                ticker = exchange.fetch_ticker(symbol)
                prices[exchange_id] = ticker['last']
            except Exception as e:
                logging.error(f"Error fetching price from {exchange_id}: {e}")
        return prices

    def place_market_order(self, symbol, order_type, amount):
        responses = {}
        for exchange_id, exchange in self.exchanges.items():
            try:
                if order_type == 'buy':
                    response = exchange.create_market_buy_order(symbol, amount)
                elif order_type == 'sell':
                    response = exchange.create_market_sell_order(symbol, amount)
                else:
                    raise ValueError('Order type must be "buy" or "sell"')
                responses[exchange_id] = response
            except Exception as e:
                logging.error(f"Error placing order on {exchange_id}: {e}")
        return responses
