#!/bin/python

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    sub = "hackerrank"
    j = 0
    for p in s:
        if p == sub[j]:
            j+=1
            if j == len(sub):
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
