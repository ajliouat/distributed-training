import argparse
import yaml
from src.pipeline_parallelism import PipelineParallelism
from src.zero_redundancy_optimizer import ZeroRedundancyOptimizer
from src.communication_patterns import CommunicationPatterns
from src.sharding_strategies import ShardingStrategies

def main(config):
    # Initialize components
    pipeline = PipelineParallelism(config['pipeline_parallelism'])
    zero = ZeroRedundancyOptimizer(config['zero_redundancy'])
    comm = CommunicationPatterns(config['communication_pattern'])
    sharding = ShardingStrategies(config['sharding_strategy'])

    # Run training
    print("Starting distributed training...")
    pipeline.run()
    zero.apply()
    comm.optimize()
    sharding.apply()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    main(config)