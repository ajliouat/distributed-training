import time
from src.pipeline_parallelism import PipelineParallelism
from src.zero_redundancy_optimizer import ZeroRedundancyOptimizer
from src.communication_patterns import CommunicationPatterns
from src.sharding_strategies import ShardingStrategies

def benchmark_training():
    pipeline = PipelineParallelism(True)
    zero = ZeroRedundancyOptimizer(True)
    comm = CommunicationPatterns("ring")
    sharding = ShardingStrategies("auto")

    start_time = time.time()
    pipeline.run()
    zero.apply()
    comm.optimize()
    sharding.apply()
    end_time = time.time()

    print(f"Training completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    benchmark_training()