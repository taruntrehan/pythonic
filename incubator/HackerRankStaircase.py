def staircase(n):
    
    for i in range(1,n+1):
        #print(i)
        blankCtr=n-i
        startCtr=n-blankCtr
        #print(blankCtr)
        #print(startCtr)
        blankStr=""
        startStr=""
        for x in range(blankCtr):
            blankStr=blankStr+" "
        for y in range(startCtr):
            startStr=startStr+"#"
        print(blankStr+startStr)
    
staircase(6)
