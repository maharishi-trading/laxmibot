import time

class StrategyExecutor:
    def __init__(self, strategy, tick_interval):
        self.strategy = strategy
        self.tick_interval = tick_interval

    def start(self):
        while True:
            self.strategy.execute()
            time.sleep(self.tick_interval)
