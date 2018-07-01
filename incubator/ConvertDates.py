def timeConversion(s):
    inputSubString=s[-2:]
    print(inputSubString)
    timeStringForAct=s[:-2]
    hourString=s[:2]
    print(hourString)
    print(timeStringForAct)
    restString=s[2:8]
    print(restString)
    if inputSubString=="PM":
        print("1")
        if hourString=="12":
            hourString="12"
        else:
            hourString=int(hourString)+int("12")
        print(hourString)
    if inputSubString=="AM":
        amHourStr=int(hourString)
        if amHourStr==12:
            hourString="00"    
    strFinStr=str(hourString)+str(restString)
    print(strFinStr)
    return strFinStr   
timeConversion("12:40:22AM")