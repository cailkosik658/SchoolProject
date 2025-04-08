def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else None
    return average

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average is:", average)
