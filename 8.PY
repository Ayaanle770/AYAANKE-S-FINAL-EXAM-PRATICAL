



def capitalize_list_items(lst):
    """
    Returns a list with each item capitalized.

    Parameters:
    lst (list of str): The list of strings to be capitalized.

    Returns:
    list of str: The list with each item capitalized.
    """
    return [item.capitalize() for item in lst]

if __name__ == "__main__":
  
    sample_list = ['apple', 'banana', 'cherry']
    capitalized_list = capitalize_list_items(sample_list)
    print(capitalized_list)  # ['Apple', 'Banana', 'Cherry']
