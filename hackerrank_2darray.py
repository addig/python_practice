#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rowN = len(arr)
    colN = len(arr[0])
    sum_list = list()
    for i in range(rowN):
        for j in range(colN):
                if (i<rowN-2) & (j<colN-2):
                    sum_list = sum_list+[(arr[i+0][j+0]+arr[i+0][j+1]+arr[i+0][j+2]+arr[i+1][j+1]+arr[i+2][j+0]+arr[i+2][j+1]+arr[i+2][j+2])]
    return max(sum_list)
if __name__ == '__main__':

    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)
    print result

