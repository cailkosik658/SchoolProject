def find_missing_number(nums):
    """
    Find missing number in the given list of numbers.
    
    Args:
    nums (List[int]): A list of integers where one integer is missing from the list.
    
    Returns:
    int: The missing number in the list. If there are no duplicates, returns 0.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage and check function
def check_solution():
    assert find_missing_number([4, 7, 2]) == 5, "Test case 1 failed"
    assert find_missing_number([3, 0, 1]) == 2, "Test case 2 failed"
    assert find_missing_number([9, 6, 4, 2, 8, 1]) == 5, "Test case 3 failed"

check_solution()
