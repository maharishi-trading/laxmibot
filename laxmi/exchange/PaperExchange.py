import logging

from laxmi.exchange.AbstractExchange import AbstractExchange

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PaperExchange(AbstractExchange):
    def __init__(self, exchange_class):
        super().__init__()
        self.balances = {'BTC': 0.01, 'ETH': 0.10, 'EUR': 100}  # Instance-level balance
        self.exchange = exchange_class()  # Initialize real exchange class for data
        self.order_book = []

    def create_market_buy_order(self, symbol, amount):
        # Simulate market buy order
        ticker = self.fetch_ticker(symbol)
        if ticker is None:
            return {'info': 'Failed to fetch market data for order simulation'}

        simulated_price = ticker['last']
        cost = simulated_price * amount
        base_currency, quote_currency = symbol.split('/')

        # Check if enough balance is available
        if self.balances.get(quote_currency, 0) < cost:
            return {'info': 'Insufficient balance for market buy order'}

        self.balances[quote_currency] -= cost
        self.balances[base_currency] += amount
        self.order_book.append({
            'symbol': symbol,
            'type': 'market',
            'side': 'buy',
            'amount': amount,
            'price': simulated_price
        })
        return {'info': 'Market buy order simulated', 'filled': amount, 'cost': cost}

    def create_market_sell_order(self, symbol, amount):
        # Simulate market sell order
        ticker = self.fetch_ticker(symbol)
        if ticker is None:
            return {'info': 'Failed to fetch market data for order simulation'}

        simulated_price = ticker['last']
        revenue = simulated_price * amount
        base_currency, quote_currency = symbol.split('/')

        # Check if enough of the base currency is available to sell
        if self.balances.get(base_currency, 0) < amount:
            return {'info': 'Insufficient amount of base currency for market sell order'}

        self.balances[base_currency] -= amount  # Reduce the base currency
        self.balances[quote_currency] += revenue  # Increase the quote currency
        self.order_book.append({
            'symbol': symbol,
            'type': 'market',
            'side': 'sell',
            'amount': amount,
            'price': simulated_price
        })
        return {'info': 'Market sell order simulated', 'filled': amount, 'revenue': revenue}
