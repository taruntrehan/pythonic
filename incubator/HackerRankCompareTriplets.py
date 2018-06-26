def solve(aliceArr, bobArr):
    retArr=[0,0]
    for i in [0,1,2]:
        if aliceArr[i]>=1 and aliceArr[i]<=100 and bobArr[i]>=1 and bobArr[i]<=100:
            print("Valid row.")
            if aliceArr[i]>bobArr[i]:
                retArr[0]=retArr[0]+1
            if aliceArr[i]<bobArr[i]:
                retArr[1]=retArr[1]+1
    return retArr
retArrVal=solve([-3,6,7],[3,6,-10])
print(retArrVal)