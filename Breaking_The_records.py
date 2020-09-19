#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    h=0
    l=0
    high=scores[0]
    low=scores[0]
    for i in range(len(scores)):
        
        if scores[i]>high:
            h+=1
            high=scores[i]
            print(scores[i])
        elif scores[i]<low:
            l+=1
            low=scores[i]
        else:
            pass
    return (h,l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
