#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(u):
    #
    # Write your code here.
    #
    
    h, m, s = map(int, u[:-2].split(':'))
    p = u[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return(('%02d:%02d:%02d') % (h, m, s))
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
