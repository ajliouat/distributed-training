class ZeroRedundancyOptimizer:
    def __init__(self, enabled):
        self.enabled = enabled

    def apply(self):
        if self.enabled:
            print("Applying Zero Redundancy Optimizer...")
        else:
            print("Zero Redundancy Optimizer disabled.")