# Author: Kento Woolery
# Class: CS325 - Analysis of Algorithms
# Homework 1, Problem 4, Insertion Sort
# Description: Reads inputs from a file called 'data.txt' where the first value of each line is the number of integers
#   that need to be sorted, followed by the integers.
#   Example values for data.txt:
#       4 19 2 5 11
#       8 1 23 4 5 6 1 2
#   The output will be written to a file “insert.out”.
#   For the above example the output would be:
#       19 11 5 2
#       6 5 43 2 2 1 1


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


def fileInsertSort():
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
                integers = integers[1:count+1]
                insertSort(integers)
                integers += '\n'
                numArray += integers
                line = outfile.readline()

        with open('insert.out', "w") as infile:
            for number in numArray:
                infile.write(str(number))
                if number != '\n':
                    infile.write(" ")


    except FileNotFoundError:
        print("File not found.")


def main():
    fileInsertSort()


if __name__ == "__main__":
    main()
