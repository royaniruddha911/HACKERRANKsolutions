# An integer  is a divisor of an integer  if the remainder of  n %d =0 

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    
    temp = n
    count = 0
    while temp != 0:
          
        # Fetching each digit 
        # of the number
        d = temp % 10
        temp //= 10
      
        # Checking if digit is greater
        # than 0 and can divides n.
        if d > 0 and n % d == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
