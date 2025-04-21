def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    area = length * width
    return area

# Example usage
length = 10
width = 5
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")