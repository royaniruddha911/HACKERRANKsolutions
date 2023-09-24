# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acaceptable

# Example
#  arr = [1,1,0,-1,-1]
# There are  elements, two positive, two negative and one zero. Their ratios are
#  2/5 = 0.400000
#  2/5 = 0.400000
#  1/5 = 0.200000
 
#  Results are printed as
 
#  0.400000
# 0.400000
# 0.200000


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    count_p = 0
    count_n = 0 
    count_z = 0
    for i in range(n):
        if arr[i] > 0:
            count_p = count_p +1
        if arr[i] == 0:
            count_z = count_z +1 
        if arr[i] < 0:
            count_n = count_n +1 
            
    pcp= count_p/n
    pcn = count_n/n
    pcz = count_z/n
    
    print(pcp)
    print(pcn)
    print(pcz)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

 