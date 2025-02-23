from src.pipeline_parallelism import PipelineParallelism

def test_pipeline_parallelism():
    pipeline = PipelineParallelism(True)
    pipeline.run()

if __name__ == "__main__":
    test_pipeline_parallelism()