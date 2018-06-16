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

cssStr = "<link href=\"<spring:url value=\"/resources/css/mainv2.css\"/>\" rel=\"stylesheet\">"
print(cssStr)
indexCssNm = cssStr.find("mainv2.css")
print(str(indexCssNm))
cssSub=cssStr[0:46]
print(cssSub)
cssRev=cssSub[::-1]
print(cssRev)
cssFirstIdx=cssRev.find("\"")
print(str(cssFirstIdx))
cssRev=cssRev[0:15]
print(cssRev)
cssRev=cssRev[::-1]
print(cssRev)