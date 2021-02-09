#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum=scores[0]
    maximum=scores[0]
    most=0
    least=0
    for i in range(len(scores)):
        if scores[i]>maximum:
            maximum=scores[i]
            most+=1
        elif scores[i]<minimum:
            minimum=scores[i]
            least+=1
    return most,least

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
