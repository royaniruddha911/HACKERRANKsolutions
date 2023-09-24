# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example
# arr = [1,3,5,7,9]
# The minimum sum is 1+3_5+7 = 16 and the maximum sum is 3 +5 + 7 + 9 = 24. The function prints
# 16 24


# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of 5 integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    L = len(arr)
    x = 0
    for i in range(L):
        x = x + arr[i]
    
    maxe = arr[0] # Initialize maximum element
    mine = arr[0]  # Initialize minimum element
    for i in range(1, L):
        if arr[i] > maxe:
            maxe = arr[i] # and compare every element with
            # current max
        if arr[i] < mine: # and compare every element with
        # current min
            mine = arr[i]
            
    print (x-maxe , x-mine)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
