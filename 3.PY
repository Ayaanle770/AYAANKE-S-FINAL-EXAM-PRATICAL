
import math

def area_of_circle(r):
    """
    Returns the area of a circle given its radius.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * r * r

if __name__ == "__main__":
    # Example usage
    radius = 5
    area = area_of_circle(radius)
    print(f"The area of a circle with radius {radius} is: {area}")
