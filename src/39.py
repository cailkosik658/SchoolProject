def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
    """
    return length * width

def main():
    # Example usage
    print("Area of rectangle with length 5 and width 3:", calculate_area(5, 3))
    
if __name__ == "__main__":
    main()
