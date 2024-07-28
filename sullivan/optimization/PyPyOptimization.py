from sullivan.optimization.OptimizationInterface import OptimizationInterface


class PyPyOptimization(OptimizationInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def optimize(self):
        # PyPy optimization logic here
        print(f"Applying PyPy optimization to {self.file_path}")

    def get_name(self):
        return "PyPy Optimization"