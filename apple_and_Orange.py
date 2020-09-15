#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app=[]
    ora=[]
    counta=0
    counto=0
    for i in range(len(apples)):
        app.append(a+apples[i])
        if app[i]>=s and app[i]<=t:
            counta+=1
    print(counta)
    for i in range(len(oranges)):
        ora.append(b+oranges[i])
        if ora[i]>=s and ora[i]<=t:
            counto+=1
    print(counto)
    
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
