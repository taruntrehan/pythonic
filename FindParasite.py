import os , sys
from os import listdir
from os.path import isfile, join

cssScanPath = "/Users/ttrehan/git/pod/src/main/webapp/resources/"
htmlScanPath = "/Users/ttrehan/git/pod/src/main/webapp/WEB-INF/jsp"
dirs = os.listdir(cssScanPath)

cssFileNmSet = set();
# This would print all the files and directories
#for file in dirs:
#   print(file)

# Scan CSS Path and check for files that contain css definition.
for root, dirs, files in os.walk(cssScanPath, topdown=True):
    #print("Root Dir"+str(root))
    for name in files:
        fullQualName = os.path.join(root, name)
        fileName = os.path.basename(fullQualName)
        if(fileName.find("css")!=-1):
            #print(fullQualName)
            cssFileNmSet.add(fullQualName)

#for x in cssFileNmSet:
#    print(x)

# Scan HTML/JSP input folder and prepare a master set.
for jspFileNm in listdir(htmlScanPath):
    if isfile(join(htmlScanPath,jspFileNm)):
        fullJspPath = join(htmlScanPath,jspFileNm);
        #print(fullJspPath)


with open("/Users/ttrehan/git/pod/src/main/webapp/WEB-INF/jsp/head.jsp") as inpFile:
    for currLine in inpFile:
        #print(currLine)
        if((currLine.find(".css")!=-1 or currLine.find("stylesheet")!=-1) and currLine.find("http")==-1):
            #print(currLine)
            indexCssNm = currLine.find(".css")+4
            #print(str(indexCssNm))
            cssSub = currLine[0:indexCssNm]
            #print(cssSub)
            cssRev = cssSub[::-1]
            #print(cssRev)
            cssFirstIdx = cssRev.find("\"")
            #print(str(cssFirstIdx))
            cssRev = cssRev[0:cssFirstIdx]
            #print(cssRev)
            cssRev = cssRev[::-1]
            print("Final inclusion string:"+cssRev)


#onlyfiles = [f for f in listdir(htmlScanPath) if isfile(join(htmlScanPath, f))]
#print(onlyfiles)

# Output File Format : CSS Master (All CSS Files Listing)
# File Path , File Name
#
# Output File Format : CSS Master (All CSS Files Listing)
# JSP File Path , JSP File Name , CSS Inclusion Line , CSS Inclusion File Name , CSS Inclusion Path
#


