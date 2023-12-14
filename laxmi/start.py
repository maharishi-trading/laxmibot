import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import json
import ccxt

from laxmi.PaperExchange import PaperExchange


class MultiExchangeCryptoBot:
    def __init__(self, exchange_credentials, paper_trading_config):
        self.exchanges = {}
        for exchange_id, credentials in exchange_credentials.items():
            exchange_class = getattr(ccxt, exchange_id)
            if paper_trading_config.get(exchange_id, False):
                # Initialize a paper trading exchange
                self.exchanges[exchange_id] = PaperExchange(exchange_class=exchange_class)
            else:
                # Initialize a real exchange

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

    def run(self, symbol, order_type, amount):
        prices = self.fetch_price(symbol)
        logging.info("Current prices: %s", json.dumps(prices, indent=4, sort_keys=True))

        orders = self.place_market_order(symbol, order_type, amount)
        # pretty print the response
        logging.info("Orders: %s", json.dumps(orders, indent=4, sort_keys=True))


# load Exchange credentials from a module
from keys.do_not_share_credentials import dont_share_credentials as exchange_credentials

paper_trading_config = {
    # Configuration to indicate which exchanges are for paper trading
    'kraken': True,
    'bitstamp': True,
    'cryptocom': True
}

bot = MultiExchangeCryptoBot(exchange_credentials(), paper_trading_config)

bot.run('BTC/EUR', 'sell', 0.0003)