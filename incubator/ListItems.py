# Input list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Iterate List
for i in a:
    if i>5:
        print("This number is less than 5:"+str(i))

# try the same code in one line.
print ([x for x in [3,4,7,8] if x<5])