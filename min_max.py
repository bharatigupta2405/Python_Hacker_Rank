#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    li=sorted(arr)
    min=0
    max=0
    for i in range(4):
        min+=li[i]
    for j in range(4,0,-1):
        max+=li[j]
        
    print(f'{min} {max}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
