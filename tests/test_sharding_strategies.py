from src.sharding_strategies import ShardingStrategies

def test_sharding_strategies():
    sharding = ShardingStrategies("auto")
    sharding.apply()

if __name__ == "__main__":
    test_sharding_strategies()