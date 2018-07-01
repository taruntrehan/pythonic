def miniMaxSum(arr):
    # print(arr)
    arrAsc=sorted(arr)
    # print(arrAsc)
    arrDesc=sorted(arr,reverse=True)
    # print(arrDesc)
    minSum=0
    maxSum=0
    i=0
    while i<4:
        minSum=minSum+arrAsc[i]
        i=i+1
    j=0
    while j<4:
        #print(arrDesc[j])
        maxSum=maxSum+arrDesc[j]
        j=j+1

    print(str(minSum)+" "+str(maxSum))

miniMaxSum([1,2,3,4,5])