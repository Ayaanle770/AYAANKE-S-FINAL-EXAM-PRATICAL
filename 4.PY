


def convert_celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in degrees Celsius.

    Returns:
    float: Temperature in degrees Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    # Example usage
    temp_celsius = 25
    temp_fahrenheit = convert_celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C is {temp_fahrenheit}°F")
