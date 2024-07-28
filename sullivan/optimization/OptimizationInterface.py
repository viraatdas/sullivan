from abc import ABC, abstractmethod

class OptimizationInterface(ABC):
    @abstractmethod
    def optimize(self):
        pass

    @abstractmethod
    def get_name(self):
        pass