import ccxt
import time

class MultiExchangeCryptoBot:
    def __init__(self, exchange_credentials):
        self.exchanges = {}
        for exchange_id, credentials in exchange_credentials.items():
            exchange_class = getattr(ccxt, exchange_id)
            self.exchanges[exchange_id] = exchange_class({
                'apiKey': credentials['api_key'],
                'secret': credentials['api_secret']
            })

    def fetch_price(self, symbol):
        prices = {}
        for exchange_id, exchange in self.exchanges.items():
            try:
                ticker = exchange.fetch_ticker(symbol)
                prices[exchange_id] = ticker['last']
            except Exception as e:
                print(f"Error fetching price from {exchange_id}: {e}")
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
                print(f"Error placing order on {exchange_id}: {e}")
        return responses

    def run(self, symbol, order_type, amount):
        prices = self.fetch_price(symbol)
        print("Current prices:", prices)

        orders = self.place_market_order(symbol, order_type, amount)
        print("Orders placed:", orders)

# load Exchange credentials from a module
from keys.dont_share_credentials import dont_share_credentials

# Instantiate and run the bot
bot = MultiExchangeCryptoBot(dont_share_credentials())
bot.run('BTC/EUR', 'buy', 0.0000900)
