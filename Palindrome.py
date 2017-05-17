inpStr = "nitin"
print("Input String is:"+inpStr)
length = inpStr.__len__();
print("Input String length:"+str(length))
revStr = inpStr[::-1]
print("reversed String:"+revStr)
if inpStr.__eq__(revStr):
    print("String is palindrome")
else:
    print("Not palindrome")
