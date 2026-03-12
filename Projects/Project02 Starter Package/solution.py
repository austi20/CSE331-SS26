"""
Project 2
CSE 331 SS26
solution.py
"""


from typing import Callable, List, TypeVar


T = TypeVar("T")  # represents generic type


# This is an optional helper function but HIGHLY recommended, especially for the application problem!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compare elements first and second and return `True` if `first` should come before `second`
    Takes custom comparator and whether the sort will be descending into account

    :param first: First value to compare
    :param second: Second value to compare
    :param comparator: Function which performs comparison
    :param descending: Determines whether comparison result should be flipped
    :return: True if first should come before second in a sorted list
    """
    if descending:
        return comparator(second, first)
    return comparator(first, second)


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list in place using selection sort algorithm.

    :param data: List of type T to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
     treated as less than or equal to the second argument.
    :param descending: Perform the sort in descending order when this is True
    """
    n = len(data)
    for i in range(n):
        selected = i
        for j in range(i + 1, n):
            if do_comparison(data[j], data[selected], comparator, descending):
                selected = j
        if selected != i:
            data[i], data[selected] = data[selected], data[i]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sorts a list in place using bubble sort algorithm.

    :param data: List of type T to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
     treated as less than or equal to the second argument.
    :param descending: Perform the sort in descending order when this is True
    """
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if do_comparison(data[j + 1], data[j], comparator, descending):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list in place using insertion sort algorithm.

    :param data: List of type T to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
     treated as less than or equal to the second argument.
    :param descending: Perform the sort in descending order when this is True
    """
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and do_comparison(current, data[j], comparator, descending):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts a list in-place using a hybrid sort with the merge sort and insertion sort algorithms
    Uses insertion_sort to sort lists once their size is less than or equal to threshold,
    and otherwise performs a merge sort

    :param data: List of type T to be sorted
    :param threshold: Maximum size at which insertion sort will be used instead of merge sort
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
     treated as less than or equal to the second argument.
    :param descending: Perform the sort in descending order when this is True
    """
    n = len(data)
    if n <= 1:
        return
    if n <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
        return

    mid = n // 2
    left = data[:mid]
    right = data[mid:]

    hybrid_merge_sort(left, threshold=threshold, comparator=comparator, descending=descending)
    hybrid_merge_sort(right, threshold=threshold, comparator=comparator, descending=descending)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if do_comparison(left[i], right[j], comparator, descending):
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

####################################################################
# DO NOT MODIFY - You are NOT required to implement quicksort.
####################################################################
def quicksort(data: List[T]) -> None:
    """
    Sorts a list in place using quicksort

    :param data: Data to sort
    """
    def quicksort_inner(first: int, last: int) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


###########################################################
# DO NOT MODIFY
###########################################################
class Product:
    """
    Class that represents products.
    """
    __slots__ = ['price', 'rating', 'relevance']

    def __init__(self, price: float, rating: int, relevance: float) -> None:
        """
        Constructor for the Product class.

        :param price: The price of the product.
        :param rating: The rating of the product.
        :param relevance: A score representing how closely the product matches the user's search keywords. A higher value
        indicates a stronger match between the product and the search query.
        :return: None
        """
        self.price = price
        self.rating = rating
        self.relevance = relevance

    def __repr__(self) -> str:
        """
        Represent the Product as a string.

        :return: Representation of the product.
        """
        return str(self)

    def __str__(self) -> str:
        """
        Convert the Product to a string.

        :return: String representation of the product.
        """
        return f'<price: {self.price}, rating: {self.rating}, relevance: {self.relevance}>'

    def __eq__(self, other) -> bool:
        """
        Compare two Product objects for equality based on price and rating.

        :param other: The other Product to compare with.
        :return: True if products are equal, False otherwise.
        """
        return self.price == other.price and self.rating == other.rating and self.relevance == other.relevance


###########################################################
# MODIFY BELOW
###########################################################
def recommend_products(products: List[Product], sorted_by: str) -> List[Product]:
    """
    Function that returns the sorted list of products that are relevant to the user's search keywords.
    NOTE: Implemented in a way that uses no extra space besides that used hybrid_merge_sort.

    :param products: a list of products waiting to be sorted.
    :param sorted_by: the metric to sort the list of products. (1) If 'rating', sort by rating in descending order;
    if two products have the same rating, then sort by price in ascending order. (2) If 'price_low_to_high', sort
    products by price in ascending order; if two products have the same price, then sort by rating in descending order.
    (3) If 'price_high_to_low', sort products by price in descending order; if two products have the same price, then
    sort by rating in descending order. If two products share the same price and rating, their order doesn't matter.
    :return: List[Product]. Sorted list of products that are relevant to the user's search keywords.
    """
    if not products:
        return []

    hybrid_merge_sort(products, comparator=lambda a, b: a.relevance < b.relevance, descending=True)
    keep = int(len(products) * 0.3 + 0.5)
    relevant = products[:keep]

    if sorted_by == 'price_low_to_high':
        comp = lambda a, b: (a.price < b.price) or (a.price == b.price and a.rating > b.rating)
    elif sorted_by == 'price_high_to_low':
        comp = lambda a, b: (a.price > b.price) or (a.price == b.price and a.rating > b.rating)
    else:
        comp = lambda a, b: (a.rating > b.rating) or (a.rating == b.rating and a.price < b.price)
    hybrid_merge_sort(relevant, comparator=comp)
    return relevant