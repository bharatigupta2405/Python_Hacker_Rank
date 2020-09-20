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
    rsum=0
    lsum=0
    diff=0
    k=0
    n=len(arr)
    for i in range(len(arr)):
        lsum+=arr[i][i]
        print(lsum)
    for j in range(len(arr)-1,-1,-1):
        rsum+=arr[k][j]
        k+=1
        print(rsum)
    if lsum>rsum:
        diff=lsum-rsum
    else:
        diff=rsum-lsum
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
