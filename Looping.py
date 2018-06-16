inpVal = int(input("Enter loop limit"))
i=0
while(i<inpVal):
    print("Value of :"+str(i))
    i+=1
print("End of while loop demo")

for x in range(inpVal):
    print("Printing x"+str(x))
print("End of range loop")

for x in [1,2]:
    print("Printing x"+str(x))
print("End of static array loop")
