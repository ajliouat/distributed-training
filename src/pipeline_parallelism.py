class PipelineParallelism:
    def __init__(self, enabled):
        self.enabled = enabled

    def run(self):
        if self.enabled:
            print("Running pipeline parallelism...")
        else:
            print("Pipeline parallelism disabled.")