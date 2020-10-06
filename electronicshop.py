#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    l=[]
    if(keyboards>drives):
        for i in range(len(keyboards)):
            for j in range(len(drives)):
                total=0
                total=keyboards[i]+drives[j]
                if total<=b:
                    l.append(total)
                else:
                    pass
            
    else :
        for j in range(len(drives)):
            for i in range(len(keyboards)):
                total=0
                total=keyboards[i]+drives[j]
                if total<=b:
                    l.append(total)
                else:
                    pass
    if len(l)==0:
        return -1
    else:
        return max(l)
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
