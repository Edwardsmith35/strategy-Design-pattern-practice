from .strategy_interface import (
    DiscountStrategy,
)  


class NoDiscount(DiscountStrategy):
    def apply_discount(self, order_total: float) -> float:
        print("No Discount Applied!")
        return order_total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount_percent):
        if not (0 <= discount_percent <= 100):
            raise ValueError("discount_percent must be between 0 and 100")
        self.discount_percent = discount_percent

    def apply_discount(self, order_total: float):
        print(f"Applying {self.discount_percent}% discount")
        return order_total * (1 - self.discount_percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    """Applies a fixed amount discount, but not more than the order total."""
    def __init__(self, fixed_discount: float):
        if fixed_discount < 0:
            raise ValueError("fixed_discount can't be Negative")
        self.fixed_discount = fixed_discount

    def apply_discount(self, order_total: float):
        if self.fixed_discount > order_total:
            raise ValueError("fixed_discount Can't be more than the order total!")
        print(f"Applying fixed ${self.fixed_discount:.2f} discount")
        return order_total - self.fixed_discount
