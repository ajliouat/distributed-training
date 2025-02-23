class ShardingStrategies:
    def __init__(self, strategy):
        self.strategy = strategy

    def apply(self):
        print(f"Applying {self.strategy} sharding strategy...")