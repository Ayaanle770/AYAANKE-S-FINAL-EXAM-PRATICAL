



def reverse_list(arr):
    """
    Returns the reverse of the given array.

    Parameters:
    arr (list): The array to be reversed.

    Returns:
    list: The reversed array.
    """
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

if __name__ == "__main__":
    # Example usage
    print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
    print(reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]
