import logging
from typing import Dict

import ccxt

# load Exchange credentials from a module
import keys.do_not_share_credentials
from laxmi.exchange.AbstractExchange import AbstractExchange
from laxmi.exchange.LaxmiExchange import LaxmiExchange
from laxmi.exchange.PaperExchange import PaperExchange
from laxmi.executor.StrategyExecutor import StrategyExecutor
from strategies.trading_strategies.VwapStrategy import VwapStrategy

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MultiExchangeCryptoBot:
    def __init__(self, exchange_cred, paper_trad_config):
        self.exchanges: Dict[str, AbstractExchange] = {}
        for exchange_id, credentials in exchange_cred.items():
            exchange_class = getattr(ccxt, exchange_id)
            if paper_trad_config.get(exchange_id, False):
                # Initialize a paper trading exchange
                self.exchanges[exchange_id] = PaperExchange(exchange_class=exchange_class)
            else:
                # Initialize a real exchange
                self.exchanges[exchange_id] = LaxmiExchange(exchange_class({
                    'apiKey': credentials['api_key'],
                    'secret': credentials['api_secret']
                })
                )

paper_trading_config = {
    # Configuration to indicate which exchanges are for paper trading
    'kraken': True,
    'bitstamp': True,
    'cryptocom': True
}

bot = MultiExchangeCryptoBot(keys.do_not_share_credentials.dont_share_credentials(), paper_trading_config)

# Example of initializing and starting a strategy
strategy = VwapStrategy(bot.exchanges)
executor = StrategyExecutor(strategy, 1)  # Executes every second

# In a separate thread or process, you might start the executor
executor.start()
