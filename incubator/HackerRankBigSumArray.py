import math
import os
import random
import re
import sys

def aVeryBigSum(inputArr):
    arrLen=len(inputArr)
    print("Array Size:"+str(arrLen))
    if arrLen>=1 and arrLen<=10:
        print("Iterating array")
        sumVal=0
        for x in inputArr:
            if x>=0 and x<=10000000000:
                print("Valid")
                sumVal=int(sumVal)+int(x);
    print("SumVal:"+str(sumVal))
retArrVal=aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005])