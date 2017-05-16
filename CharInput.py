import datetime
# Get Input Name
name = input("Please enter your name:")
print(name)
# Get Input Age
age = input("Please enter your age:")
age = int(age)
print(age)
# Get Difference From 100 Years
diff = 100-age
print(diff)
# Get Current Date
now = datetime.datetime.now()
print(now)
# Get Current Year
currYear=int(now.year)
print(currYear)
# Add Difference and print
hundredYear = currYear+diff;
print("You will be hundred Years Old in"+ str(hundredYear))