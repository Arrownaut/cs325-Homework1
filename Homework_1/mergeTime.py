# Author: Kento Woolery
# Class: CS325 - Analysis of Algorithms
# Homework 1, Problem 5, Merge Sort Timing
# Description: Generates arrays of random numbers and sorts them via merge sort.
# # Uses the system clock to time how long it takes to sort each of the arrays of increasing size and
# # prints it to the console.


import time
import random
import functools


def sort_timer(function):
    """Adds timers as wrappers to passed function to determine run-time of said function."""

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        """Takes the time prior to and immediately after a function's execution. returns the difference as the
        total run-time."""

        initial_time = time.perf_counter()
        function(*args, **kwargs)
        end_time = time.perf_counter()

        return end_time - initial_time

    return wrapper


@sort_timer
def timeMergeSort(array):
    """helper function to house the mergeSort function, which otherwise would mess up timing it
    due to the recursive calls."""
    mergeSort(array)
    return

def mergeSort(sorted_array):
    """
    sorts a passed array in descending order via merge sort methods
    """
    if len(sorted_array) > 1:
        mid = len(sorted_array) // 2
        left = mergeSort(sorted_array[:mid])
        right = mergeSort(sorted_array[mid:])

        left_index = 0
        right_index = 0

        sorted_array = []

        while left_index < len(left) and right_index < len(right):
            """While there are still numbers in both the left and right halves, pop whichever has the
            greater value and push it onto the array for a descending sort"""
            if left[left_index] > right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1

        """Once there are no longer numbers in either the right or left half..."""
        while left_index < len(left):
            """If the left half still has numbers, simply add them"""
            sorted_array.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            """If the right half still has numbers, simply add them"""
            sorted_array.append(right[right_index])
            right_index += 1
    return sorted_array


def rng(sample_size):
    """returns a list of random numbers between 1 and 10000. passed argument determines how long the list is."""
    random_nums = []
    for i in range(sample_size):
        random_nums.append(random.randint(1, 10000))
    return random_nums


def main():
    """runs a sort of increasingly large arrays of randomly generated numbers.
    prints sample size and time to sort to the console"""
    n = 2000
    print("Sample Size\t|\t", "Time to Sort (in seconds)")
    while n <= 20000:
        print(n, '\t\t\t', timeMergeSort(rng(n)))
        n += 2000
    return


if __name__ == '__main__':
    main()
