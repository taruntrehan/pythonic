def dedupe(inputStr):
    y = []
    for i in inputStr:
        if i not in y:
            y.append(i)
    return y
a = [1,2,3,4,1,2]
print(a)
print(dedupe(a))