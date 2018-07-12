def setOperations(inputSetObj):
    print(inputSetObj)
    print('brown' in inputSetObj)
    for x in inputSetObj:
        print(x)

# Input list
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
setOperations(basket)