# Get Input Number
number = input("Enter number")
number = int(number)
div = number%2
print(div)
if number % 2 == 0:
    print("Its an even number")
else:
    print("Its an odd number")