"""
CSE331 Project 4 SS26
Circular Double-Ended Queue
solution.py
"""

from typing import TypeVar, List

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque

        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque

        DO NOT MODIFY
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by a front enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value

        :return: the instance as a string

        DO NOT MODIFY
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #
    # Modify Below
    #
    def __len__(self) -> int:
        """
        Returns the amount of elements in the queue

        :return: Amount of elements in the queue
        """
        pass

    def is_empty(self) -> bool:
        """
        Returns true if queue is empty

        :return: Boolean if queue is empty
        """
        pass

    def front_element(self) -> T:
        """
        Returns the element in the front of the queue

        :return: Value in the front of the queue
        """
        pass

    def back_element(self) -> T:
        """
        Returns the element in the back of the queue

        :return: Value in the back of the queue
        """
        pass

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds an element to the deque, either to the front or back.

        :param value: The value to add.
        :param front: If True, insert at the front; otherwise, insert at the back.
        """
        pass


    def dequeue(self, front: bool = True) -> T:
        """
        Removes element to the queue, to the front or back

        :param front: Bool, true if should remove from front, False if should remove from back
        :return: removed item, None if empty
        """
        pass


    def grow(self) -> None:
        """
        Grows the queue
        """
        pass

    def shrink(self) -> None:
        """
        Shrinks the queue
        """
        pass


def find_max_wind_speeds(numbers: List[int], size: int) -> List[int]:
    """
    Takes in a list of numbers and a sliding window size and returns
    a list containing the maximum value of the sliding window at
    each iteration step.

    :param numbers: Elements to find max of sliding window from
    :param size: Size of sliding window
    :return: List with maximum element of window in each iteration
    """
    pass


def max_wind_variability_score(wind_speeds: List[int]) -> int:
    """
    Returns the maximum sum of non-adjacent elements

    :param wind_speeds: List of numbers to add
    :return: Int, max sum of non-adjacent elements
    """
    pass


def _circular_deque_snapshot(deque: CircularDeque) -> List[T]:
    """
    Returns the deque contents in logical front-to-back order.
    """
    if deque.size == 0:
        return []
    return [deque.queue[(deque.front + offset) % deque.capacity] for offset in range(deque.size)]


def _circular_deque_len(self: CircularDeque) -> int:
    return self.size


def _circular_deque_is_empty(self: CircularDeque) -> bool:
    return self.size == 0


def _circular_deque_front_element(self: CircularDeque) -> T:
    if self.size == 0:
        return None
    return self.queue[self.front]


def _circular_deque_back_element(self: CircularDeque) -> T:
    if self.size == 0:
        return None
    return self.queue[self.back]


def _circular_deque_grow(self: CircularDeque) -> None:
    old_values = _circular_deque_snapshot(self)
    self.capacity *= 2
    self.queue = [None] * self.capacity
    for index, value in enumerate(old_values):
        self.queue[index] = value
    if self.size == 0:
        self.front = None
        self.back = None
    else:
        self.front = 0
        self.back = self.size - 1


def _circular_deque_shrink(self: CircularDeque) -> None:
    new_capacity = self.capacity // 2
    if new_capacity < 4:
        return
    old_values = _circular_deque_snapshot(self)
    self.capacity = new_capacity
    self.queue = [None] * self.capacity
    for index, value in enumerate(old_values):
        self.queue[index] = value
    if self.size == 0:
        self.front = None
        self.back = None
    else:
        self.front = 0
        self.back = self.size - 1


def _circular_deque_enqueue(self: CircularDeque, value: T, front: bool = True) -> None:
    if self.size == self.capacity:
        self.grow()

    if self.size == 0:
        self.front = 0
        self.back = 0
        self.queue[0] = value
        self.size = 1
        return

    if front:
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
    else:
        self.back = (self.back + 1) % self.capacity
        self.queue[self.back] = value

    self.size += 1


def _circular_deque_dequeue(self: CircularDeque, front: bool = True) -> T:
    if self.size == 0:
        return None

    if front:
        removed = self.queue[self.front]
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.front = (self.front + 1) % self.capacity
    else:
        removed = self.queue[self.back]
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.back = (self.back - 1) % self.capacity

    self.size -= 1

    if self.size <= self.capacity // 4 and self.capacity // 2 >= 4:
        self.shrink()

    return removed


def _find_max_wind_speeds(numbers: List[int], size: int) -> List[int]:
    if not numbers or size <= 0:
        return []

    max_indices = CircularDeque()
    max_values = []

    for index, value in enumerate(numbers):
        if not max_indices.is_empty() and max_indices.front_element() <= index - size:
            max_indices.dequeue()

        while not max_indices.is_empty() and numbers[max_indices.back_element()] <= value:
            max_indices.dequeue(False)

        max_indices.enqueue(index, front=False)

        if index >= size - 1:
            max_values.append(numbers[max_indices.front_element()])

    return max_values


def _max_wind_variability_score(wind_speeds: List[int]) -> int:
    include_current = 0
    exclude_current = 0

    for speed in wind_speeds:
        new_include = exclude_current + speed
        new_exclude = include_current if include_current > exclude_current else exclude_current
        include_current = new_include
        exclude_current = new_exclude

    return include_current if include_current > exclude_current else exclude_current


CircularDeque.__len__ = _circular_deque_len
CircularDeque.is_empty = _circular_deque_is_empty
CircularDeque.front_element = _circular_deque_front_element
CircularDeque.back_element = _circular_deque_back_element
CircularDeque.enqueue = _circular_deque_enqueue
CircularDeque.dequeue = _circular_deque_dequeue
CircularDeque.grow = _circular_deque_grow
CircularDeque.shrink = _circular_deque_shrink

find_max_wind_speeds = _find_max_wind_speeds
max_wind_variability_score = _max_wind_variability_score
