from laxmi.exchange.AbstractExchange import AbstractExchange


class LaxmiExchange (AbstractExchange):
    def __init__(self, exchange_class):
        super().__init__()
        self.exchange = exchange_class()

    def create_market_buy_order(self, symbol, amount):
        return self.exchange.create_market_buy_order(symbol, amount)

    def create_market_sell_order(self, symbol, amount):
        return self.exchange.create_market_sell_order(symbol, amount)
