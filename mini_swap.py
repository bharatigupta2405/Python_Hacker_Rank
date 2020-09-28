#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap=0
    for i in range(len(arr)):
        if(i+1!=arr[i]):
            t=i
            while(arr[t]!=i+1):
                t+=1
            temp=arr[t]
            arr[t]=arr[i]
            arr[i]=temp
            swap+=1
    return swap
 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
