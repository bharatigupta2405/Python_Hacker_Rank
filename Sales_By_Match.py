#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    x=list(set(ar))
    y=sorted([(ar.count(i),i) for i in x], key=lambda x:x[0])[::-1]
    count=0
    for i in range(len(y)):
        count+=int(y[i][0]/2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
