"""
starter.py

CC5 — Array Inversion Analysis (Disorder Metric)

Implement the function `count_inversions`.

An inversion is a pair of indices (i, j) such that:
    i < j and array[i] > array[j]

Your goal is to return the total number of inversions in the array.

Performance Requirement:
    - Target time complexity: O(n log n)
    - Target space complexity: O(n)

Notes:
    - The input may contain duplicates and negative numbers.
    - Duplicate values do NOT count as inversions (comparison is strict >).
    - You may modify the array if your algorithm requires it.
"""
from __future__ import annotations
from typing import List


def count_inversions(array: List[int]) -> int:
    """
    Return the number of inversions in `array`.

    Parameters:
        array (List[int]): List of integers (may include duplicates and negatives).

    Returns:
        int: Number of inversion pairs.

    You are expected to implement an efficient algorithm.
    A naive O(n^2) solution may not pass large test cases.
    """

    if len(array) < 2:
        return 0
    temp = [0] * len(array)

    def sort_count(lo: int, hi: int) -> int:
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        inv = sort_count(lo, mid) + sort_count(mid, hi)
        i = lo
        j = mid
        k = lo
        while i < mid and j < hi:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
                inv += mid - i
            k += 1
        while i < mid:
            temp[k] = array[i]
            i += 1
            k += 1
        while j < hi:
            temp[k] = array[j]
            j += 1
            k += 1
        array[lo:hi] = temp[lo:hi]
        return inv
    return sort_count(0, len(array))
