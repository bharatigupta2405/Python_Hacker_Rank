#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    count=0
    d=n-p
    c=p-1
    if p%2==0:
        p=p+1
    if d>c:
        for i in range(1,p+1,2):
            count+=1
    else:
        for i in range(n,p+1,2):
            count+=1
    return count-1






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()