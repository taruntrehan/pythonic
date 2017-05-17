# Enter number
inputVar = int(input("Please enter number"))
print(inputVar)
# Input list
dividList = range(2,inputVar)
print(dividList)
# Iterate List
for i in dividList:
    if inputVar%int(i)==0:
        print("Divisor True--"+str(i))
print("Program Ends Here.")