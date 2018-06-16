import random

#Get one capital Letter
#Get one small letter
#Get one number between 1 and 10
#Get one special character
#Repeat these and have a password 8 in length

masterStr = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
password = "".join(random.sample(masterStr,passlen))
print("Password is:"+str(password))
