def gradingStudents(inputArr):
    returnArr=[]    
    for i in inputArr:
        nextMultipleVal=0
        # print("ScoreVal:"+str(i))
        if i>=38:
            # print("applicable for rounding of process")
            currMultiple=int(int(i)/5)
            # print("multiple:"+str(currMultiple))
            nextMultipleVal=int((currMultiple+1)*5)
            # print("nextMultipleVal:"+str(nextMultipleVal))
            diff=nextMultipleVal-i
            # print(diff)
            if diff<3:
                i=nextMultipleVal
                print(nextMultipleVal)
                returnArr.append(nextMultipleVal)
            else:
                print(i)
                returnArr.append(i)
        else:
            returnArr.append(i)
    return returnArr
        
returnVal=gradingStudents([23,80,96,18,73,78,60,60,15,45,15,10,5,46,87,33,60,14,71,65,2,5,97,0])
print(returnVal)
    
80
96
18
75
80
60
60
15
45
15
10
5
46
87
33
60
14
71
65
2
5
97
0