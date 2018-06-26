print("File Reading Witing Operation")
with open('python_sample_read_write.txt', 'w') as fileWriteObj:
    fileWriteObj.write("New Text Line Here.\n")
    fileWriteObj.write("New Text Line Here.\n")
    fileWriteObj.write("New Text Line Here.\n")
fileWriteObj.closed

fileReaderObj = open('python_sample_read_write.txt','r')
for readLine in fileReaderObj:
    print(readLine,end='')
fileReaderObj.close()
