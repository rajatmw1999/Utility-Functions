# Python program to check validation of password
# Module of regular expression is used with search()
import re

def weak_strong_password(password):
    flag = 0
    while True:
        if len(password)<8:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print("Strong Password")
            return True

    if flag ==-1:
    	print("Weak Password")
        return False

weak_strong_password(input("Please enter your password : "))