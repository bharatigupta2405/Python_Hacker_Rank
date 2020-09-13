#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero=0
    pos=0
    neg=0
    for i in range(len(arr)):
        if arr[i]==0:
            zero+=1
        if arr[i]>0:
            pos+=1
        if arr[i]<0:
            neg+=1
        
    print (f"{pos/len(arr):.6f}")
    print (f"{neg/len(arr):.6f}")
    print (f"{zero/len(arr):.6f}")



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
