from src.zero_redundancy_optimizer import ZeroRedundancyOptimizer

def test_zero_redundancy_optimizer():
    zero = ZeroRedundancyOptimizer(True)
    zero.apply()

if __name__ == "__main__":
    test_zero_redundancy_optimizer()