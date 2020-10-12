#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    l=[k for k in range(i,j+1)]
    o=l.copy()
    r=[]
    count=0
    for i in range(len(l)):
        Reverse = 0    
        while(l[i] > 0):    
            Reminder = l[i] %10    
            Reverse = (Reverse *10) + Reminder    
            l[i]= l[i]//10 
        r.append(Reverse)
    
    print(o)

    for i in range(len(o)):
        minus=r[i]-o[i]
        print(minus)
        if minus%k==0:
            count+=1
    return count
          


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
