from sullivan.optimization.OptimizationInterface import OptimizationInterface


class CythonOptimization(OptimizationInterface):
    def __init__(self, file_path):
        self.file_path = file_path

    def optimize(self):
        # Cython optimization logic here
        print(f"Applying Cython optimization to {self.file_path}")

    def get_name(self):
        return "Cython Optimization"