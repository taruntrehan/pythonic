# Input list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
finList = []
for i in a:
    if i%2==0:
        finList.append(i)
    else:
        print("Odd Number")

print(finList)
