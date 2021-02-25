#!/bin/python

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
