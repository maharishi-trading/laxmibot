import json
import logging

from laxmi.strategy.AbstractStrategy import AbstractStrategy


class VwapStrategy(AbstractStrategy):
    def __init__(self, exchanges):
        super().__init__(exchanges)

    def execute(self):
        print('Executing VWAP strategy')
        self.run('BTC/USDT', 'buy', 0.001)
        pass

    def run(self, symbol, order_type, amount):
        prices = self.fetch_price(symbol)
        logging.info("Current prices: %s", json.dumps(prices, indent=4, sort_keys=True))

        orders = self.place_market_order(symbol, order_type, amount)
        # pretty print the response
        logging.info("Orders: %s", json.dumps(orders, indent=4, sort_keys=True))
