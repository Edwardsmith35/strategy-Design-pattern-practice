from concrete_strategies import NoDiscount
from strategy_interface import DiscountStrategy


class Order:
    """
    The Context defines the interface of interest to clients.
    It maintains a reference to one of the Strategy objects.
    """

    def __init__(self, total: float, strategy: DiscountStrategy = None):
        self._total = total
        self._strategy = strategy if strategy else NoDiscount()
        print(
            f"Order Created with total: ${self.total:.2f} and Strategy: {self._strategy.__class__.__name__}"
        )

    @property  # The @property decorator is a Pythonic way to manage attribute access. It allows you to define methods that are accessed like attributes (i.e., without parentheses ()), giving you more control over getting, setting, and deleting an attribute's value.
    def total(self):
        return self._total

    def set_discount_strategy(self, strategy: DiscountStrategy):
        """Allows replacing the strategy at runtime."""
        print(f"Changing discount strategy to: {strategy.__class__.__name__}")
        self._strategy = strategy

    def get_final_price(self):
        return self._strategy.apply_discount(self.total)
