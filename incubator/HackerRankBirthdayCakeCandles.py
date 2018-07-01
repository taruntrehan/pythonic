def birthdayCakeCandles(ar):
    print(ar)
    arrDesc=sorted(ar,reverse=True)
    print(arrDesc)
    maxCandleVal=[arrDesc[0]]
    print(maxCandleVal)
    resultArr=[]
    arrCtr=0
    for i in ar:
        if(i==maxCandleVal[0]):
            print("match found")
            resultArr.append(i)
    print(resultArr)
    finListLen=resultArr.__len__()
    print("\n"+str(finListLen))
    return finListLen
birthdayCakeCandles([3,2,1,3])
birthdayCakeCandles([82,49,82,82,41,82,15,63,38,25])