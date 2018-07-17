def listComprehension(firstIntegerList,secondIntegerList):
    print(firstIntegerList,secondIntegerList)
    retArr=[[i,j] for i in firstIntegerList for j in secondIntegerList if i!=j]
    print(retArr)
listComprehension([1,2,3,4],[3,4,5,6])
