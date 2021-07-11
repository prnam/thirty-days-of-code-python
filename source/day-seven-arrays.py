#!/bin/python3

import math
import os
import random
import re
import sys


def reverse(arr):
    reverseVal = ""
    for item in range(len(arr)-1, -1, -1):
        reverseVal = reverseVal+str(arr[item])+" "
    print(reverseVal)
    return


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    reverse(arr)
