listOne = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listTwo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
finList = []
for i in listOne:
    if i in listTwo:
        print("Present:"+str(i))
        finList.append(i)
    else:
        print("Absent")
print(finList)

