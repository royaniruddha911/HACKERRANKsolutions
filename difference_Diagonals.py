#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    L = len(arr)
    sumd1= 0
    sumd2 =0
    for i in range(L):
        for j in range(L):
            if (i == j):
             sumd1 = sumd1 + arr[i][j]  
            if (j == L-i-1):
             sumd2  = sumd2 + arr[i][j]
    
    res = abs(sumd1-sumd2)
              
    
    return res    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

