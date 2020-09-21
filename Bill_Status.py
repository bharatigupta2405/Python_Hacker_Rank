#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    long=0
    for i in range(len(bill)):
        if bill[i]!=bill[k]:
            long+=bill[i]
        else:
            pass
    if (long/2)==b:
        print("Bon Appetit")
    else:
        print(int(b-(long/2)))



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
