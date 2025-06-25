from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm. The Context uses this interface to call the algorithm
    defined by Concrete Strategies.
    """
    @abstractmethod
    def apply_discount(self, order_total: float) -> float:
        pass

