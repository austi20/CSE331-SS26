def find_unsorted_subarray(array):
    """
    Finds the shortest subarray that needs to be sorted for the entire
    array to become sorted.

    Args:
        array (list of int): The input array of integers.

    Returns:
        list: A list containing two integers representing the start and
        end indices of the shortest subarray that needs to be sorted.
        If the array is already sorted, returns [-1, -1].

    To Do:
        - Students will implement the logic to find the minimum and maximum
        out-of-order elements and determine the boundaries of the subarray
        that must be sorted.
    """
    if not array or len(array) < 2:
        return [-1, -1]
    min_out = float("inf")
    max_out = float("-inf")
    for i, num in enumerate(array):
        if is_out_of_order(i, num, array):
            if num < min_out:
                min_out = num
            if num > max_out:
                max_out = num
    if min_out == float("inf"):
        return [-1, -1]
    left = 0
    while left < len(array) and array[left] <= min_out:
        left += 1
    right = len(array) - 1
    while right >= 0 and array[right] >= max_out:
        right -= 1
    return [left, right]


def is_out_of_order(i, num, array):
    """
    Helper function to determine if an element is out of order in the array.

    Args:
        i (int): The index of the element to check.
        num (int): The element at index i.
        array (list of int): The input array of integers.

    Returns:
        bool: True if the element is out of order, False otherwise.

    This function is a suggestion  to students as a helper function.
    Students are encouraged to implement this function if they find it helpful.
    """
    if len(array) < 2:
        return False
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]