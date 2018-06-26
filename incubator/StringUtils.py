import random
# Input list
inpStr = "This is Tarun Trehan"
inpStrArr = inpStr.split()
strLen = inpStrArr.__len__();
print("String lenght:"+str(strLen))
# Reversing a string here.
for i in reversed(inpStrArr):
    print(i)
indexVal = inpStr.find("i")
print(indexVal)
