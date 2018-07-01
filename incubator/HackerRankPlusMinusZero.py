def plusMinus(arr):
    arrLength=arr.__len__()
    # print(arrLength)
    zeroCtr=0
    negativeCtr=0
    positiveCtr=0
    for i in arr:
        if i==0:
            zeroCtr=zeroCtr+1
        if i<0:
            negativeCtr=negativeCtr+1
        if i>0:
            positiveCtr=positiveCtr+1
    zeroFraction=zeroCtr/arrLength
    zeroFraction=round(zeroFraction,8)   
    # print(zeroFraction)
    positiveFraction=positiveCtr/arrLength
    positiveFraction=round(positiveFraction,8)
    # print(positiveFraction)
    negativeFraction=negativeCtr/arrLength
    negativeFraction=round(negativeFraction,8)
    print("{0:.6f}".format(positiveFraction))
    print("{0:.6f}".format(negativeFraction))
    print("{0:.6f}".format(zeroFraction))
plusMinus([-4 ,3 ,-9 ,0 ,4 ,1])
