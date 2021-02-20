#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i=0
    n1=int(len(s))
    n2=int(len(t))
    min_len=min(n1,n2)
    for i in range(min_len):
        if(s[i]!=t[i]):
            break
    count=n1+n2-2*i
    if(k==count or k>=n1+n2) or (count%2==k%2 and count<=k):
        return "Yes"
    else:
        return "No"
   



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
