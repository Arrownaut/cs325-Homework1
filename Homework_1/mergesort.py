# Author: Kento Woolery
# Class: CS325 - Analysis of Algorithms
# Homework 1, Problem 4, Merge Sort
# Description: Reads inputs from a file called 'data.txt' where the first value of each line is the number of integers
#   that need to be sorted, followed by the integers.
#   Example values for data.txt:
#       4 19 2 5 11
#       8 1 23 4 5 6 1 2
#   The output will be written to a file “merge.out”.
#   For the above example the output would be:
#       19 11 5 2
#       6 5 43 2 2 1 1


def mergeSort(sorted_array):
    """
    sorts a passed array in descending order via merge sort methods.

    To avoid any claims of plagiarism,
    I first looked at descriptions and pseudocode of merge sort from the textbook and khan academy. I
    then implemented merge sort as part of the challenge in khan academy. I then used that knowledge to try
    and implement it on my own in python here and got most of the way there, but did reference geeks4geeks
    implementation when I got stuck for an extended period. Mainly, I didn't realize I
    needed to put the recursive call as a variable.
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


def fileMergeSort():
    """
    opens 'data.txt' and reads the numbers in the file, sorts each line, then outputs the sorted numbers
    to 'insert.out'
    """
    numArray = []
    try:
        with open('data.txt', "r") as outfile:
            line = outfile.readline()
            while line != '':
                integers = [int(x) for x in line.split()]
                count = integers[0]
                integers = integers[1:count + 1]
                integers = mergeSort(integers)
                integers += '\n'
                numArray += integers
                line = outfile.readline()

        with open('merge.out', "w") as infile:
            for number in numArray:
                infile.write(str(number))
                if number != '\n':
                    infile.write(" ")

    except FileNotFoundError:
        print("File not found.")


def main():
    fileMergeSort()


if __name__ == "__main__":
    main()
