def calculate_discount(price, discount_percent):
    # Calculate discount amount
    discount_amount = price * (discount_percent / 100)
    
    # Apply discount to price
    final_price = price - discount_amount
    
    return final_price

# Example usage
price = 100.00
discount_percent = 15
print("Final price after discount: ", calculate_discount(price, discount_percent))
