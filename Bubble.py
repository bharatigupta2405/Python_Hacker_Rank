#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count=0
    n=len(a)
    for k in range(n-1):
        for i in range(n-k-1):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                count+=1
                
    print(f"Array is sorted in {count} swaps. ")
    print(f"First Element: {a[0]}\nLast Element: {a[-1]}")
    

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
