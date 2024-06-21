
def check_season(month):
    """
    Returns the season for a given month.

    Parameters:
    month (str): The month of the year.

    Returns:
    str: The season corresponding to the month.
    """
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'

if __name__ == "__main__":
    # Example usage
    month = 'April'
    season = check_season(month)
    print(f"The season in {month} is: {season}")
