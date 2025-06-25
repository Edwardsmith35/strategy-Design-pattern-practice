from .concrete_strategies import NoDiscount
from .strategy_interface import DiscountStrategy

class Order():
    """
    The Context defines the interface of interest to clients.
    It maintains a reference to one of the Strategy objects.
    """
    def __init__(self, total: float, strategy: DiscountStrategy = None):
        self.total = total
        self.strategy = strategy if strategy else NoDiscount()
        print(f"Order Created with total: ${self.total:2f} and Strategy: {self.strategy.__class__.__name__}")
    
    @property
    def total(self):
        return self.total

    def set_discount_strategy(self, strategy: DiscountStrategy):
        """Allows replacing the strategy at runtime."""
        print(f"Changing discount strategy to: {strategy.__class__.__name__}")
        self._strategy = strategy
    
    def get_final_price(self):
        return self.strategy.apply_discount(self.total)