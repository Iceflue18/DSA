from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    num=arr[0]
    for i in range(1,n):
        if arr[i]>num:
            num=arr[i]
    return num
    
    
    #return max(arr)
    #sort=sorted(arr)
    #print(sort)
    #return sort[-1]
