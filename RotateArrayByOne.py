from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    left=[]
    for i in range(1,n):
        left.append(arr[i])
    left.append(arr[0])
    return left


