#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minv=arr[0]
    maxv=arr[0]
    sum1=0
    for i in range(len(arr)):
        minv=min(arr[i],minv)
        maxv=max(arr[i],maxv)
        sum1+=arr[i]
    print(str(sum1-maxv)+" "+str(sum1-minv))
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
