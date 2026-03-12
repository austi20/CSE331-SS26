
def next_greater_element(nums: list[int]) -> list[int]:
    """
    Compute the next greater element for each position in a circular array.

    For each index i in nums, find the first element that appears to the right of i
    (moving forward and wrapping around to the start if needed) that is strictly greater
    than nums[i]. If no such element exists, place -1 at that index.

    The goal is to solve this in O(n) time using a stack-based approach.

    Parameters
    ----------
    nums : list[int]
        The input list of integers.

    Returns
    -------
    list[int]
        A list where the i-th element is the next greater element for nums[i],
        or -1 if no greater element exists.
    """
    # TODO: Implement the algorithm
    # Hint:
    # - Consider using a monotonic stack to keep track of indices whose next greater
    #   element has not been found.
    # - You may need to loop through the array twice to simulate circular behavior.

    n = len(nums)
    result = [-1] * n
    stack: list[int] = []

    for i in range(2 * n):
        idx = i % n

        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]

        if i < n:
            stack.append(idx)

    return result

    # Placeholder so the function runs
    return [-1] * len(nums)
