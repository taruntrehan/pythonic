import random
# Input list
genNum = random.randint(1,9)
inpNum = int(input("Please enter a number ranging 1 to 9:"))
print("Gen Num:"+str(genNum)+"--Inp Num:"+str(inpNum))
if inpNum<genNum:
    print("Low guess")
elif inpNum>genNum:
    print("High guess")
else:
    print("Matching")

