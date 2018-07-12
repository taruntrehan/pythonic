def dictionaryOperations(inputDictionObj):
    print(inputDictionObj['112233'])
    print(list(inputDictionObj))
    keyCheck='112233' in inputDictionObj
    print(keyCheck)

    for k,v in inputDictionObj.items():
        print (k,v)    
# Input list
telObj = {"123456":"val here", "112233": ""}
dictionaryOperations(telObj)