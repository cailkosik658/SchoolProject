def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    print(calculate_average([10, 20, 30, 40]))
except ValueError as e:
    print(e)
