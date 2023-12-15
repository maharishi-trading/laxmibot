import logging
import time

from laxmi.strategy.AbstractStrategy import AbstractStrategy


class VwapStrategy(AbstractStrategy):
    def __init__(self, exchanges):
        super().__init__(exchanges)

    def execute(self):
        print('Executing VWAP strategy')
        self.run('BTC/USDT', 'buy', 0.001)

    def fetch_ohlcv(self, exchange, symbol, timeframe, ticks):
        now = int(time.time() * 1000)  # milliseconds
        one_hour_ago = now - ticks * 60 * 1000  # 60 minutes * 60 seconds * 1000 milliseconds
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=one_hour_ago, limit=ticks)
        return ohlcv

    def calculate_vwap(self, ohlcv):
        vwap_numerator = 0
        total_volume = 0
        for candle in ohlcv:
            # typical price for the period
            typical_price = (candle[1] + candle[2] + candle[3]) / 3  # Using (High + Low + Close) / 3
            volume = candle[5]
            vwap_numerator += typical_price * volume
            total_volume += volume
        return vwap_numerator / total_volume if total_volume else 0

    def get_current_price(self, exchange, symbol):
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']

    def run(self, symbol, order_type, amount):
        for exchange_id, exchange in self.exchanges.items():
            ohlcv = self.fetch_ohlcv(exchange, symbol, timeframe='1m', ticks=60)
            vwap = self.calculate_vwap(ohlcv)
            current_price = self.get_current_price(exchange, symbol)
            logging.info(f"VWAP: {vwap}, Current Price: {current_price}")
            if current_price > vwap * 1.01 and order_type == 'buy':
                logging.info(f"Buy {symbol} on {exchange_id}")
                self.place_market_order(symbol, 'buy', amount)
            else:
                if current_price < vwap * 0.99 and order_type == 'sell':
                    logging.info(f"Sell {symbol} on {exchange_id}")
                    self.place_market_order(symbol, 'sell', amount)
