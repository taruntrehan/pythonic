def diagonalDifference(arr):
    print(arr.__len__())
    arrLength=arr.__len__();
    leftDiagonalSum=0;
    rightDiagonalSum=0;
    for i in range(arrLength):
        subArrLen=arr[i].__len__();
        for j in range(subArrLen):
            if i==j:
                leftDiagonalSum=leftDiagonalSum+arr[i][j]
    print(leftDiagonalSum)
    for x in range(arrLength-1,-1,-1):
        for i in range(arr[x].__len__()):
            if x+i==arr[x].__len__()-1:
                rightDiagonalSum=rightDiagonalSum+arr[i][x]
    print(rightDiagonalSum)
    diffVal=leftDiagonalSum-rightDiagonalSum
    absDiffVal=abs(diffVal)
    print(absDiffVal)
    return absDiffVal

#11  2   4
#4   5   6
#10  8   -12
sampleArr = [[11, 2, 4], [4, 5, 6] , [10, 8, -12]]
diagonalDifference(sampleArr)