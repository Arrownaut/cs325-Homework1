# Author: Kento Woolery
# Class: CS325 - Analysis of Algorithms
# Homework 1, Problem 5, Insertion Sort Timing
# Description: Generates arrays of random numbers and sorts them via insertion sort.
# Uses the system clock to time how long it takes to sort each of the arrays of increasing size and
# prints it to the console.


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
def insertSort(arr):
    """
    sorts a passed array in descending order via insertion sort methods
    """
    for i in range(1, len(arr)):
        value = arr[i]
        position = i - 1
        while position >= 0 and arr[position] < value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = value
    return


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
        print(n, '\t\t\t', insertSort(rng(n)))
        n += 2000
    return


if __name__ == '__main__':
    main()
