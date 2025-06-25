from context import Order
from concrete_strategies import NoDiscount, PercentageDiscount, FixedAmountDiscount

def main():
    order1 = Order(1000) # Defaults to No Discount
    print(f"Order 1 Total: {order1.total}")
    print(f"Order 1 Final Price: {order1.get_final_price()}, with Strategy: {order1._strategy.__class__.__name__}")

    # Apply a percentage discount
    Discount = 5 # 5%
    percent_discount = PercentageDiscount(Discount) # 5% Discount
    order1.set_discount_strategy(percent_discount)
    print(f"Order 1 Final Price ({Discount}% Discount): {order1.get_final_price()}, with Strategy: {order1._strategy.__class__.__name__}")
    
    # Create another Order with a Fixed Discount strategy from the Start
    order2 = Order(2000, strategy=FixedAmountDiscount(100))
    print(f"Order 2 Final Price (Fixed Discount 100$): {order2.get_final_price()}, with Strategy: {order2._strategy.__class__.__name__}")
    
    # Test fixed discount that is larger than the total
    fixed_Discount_faulty = FixedAmountDiscount(3000)
    # order2.set_discount_strategy(fixed_Discount_faulty)
    # print(f"Order 2 Final Price (Faulty Fixed Discount 3000$): {order2.get_final_price()}, with Strategy: {order2._strategy.__class__.__name__}")




if __name__ == "__main__":
    main()