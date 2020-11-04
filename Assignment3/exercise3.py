# PROGRAMMING ASSIGNMENT 03
# Filename: 'exercise3.py'
#
# Password checker
# In order to be valid your password must have at least one of each: lower case letter, 
# upper case letter, digit and special character. 
# Write a program in the file exercise3.py that does the following:
# 	- asks the user to \textbf{input a password}
#	- then, prints: "This password is valid" if the password fulfills the conditions 
# 	  and prints: " This password is not valid" otherwise. 
# 
#
# WRITE YOUR CODE AFTER THIS LINE

password = input('Enter a password: ')
number = """0123456789"""
lowercase = """abcdefghijklmnopqrstuvwxyz"""
uppercase = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
specialcharacter = """"~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
number_satisfied, lowercase_satisfied, uppercase_satisfied, special_satisfied = 0, 0, 0, 0
while not (number_satisfied > 0 and lowercase_satisfied > 0 and uppercase_satisfied > 0 and special_satisfied > 0):
    for char in password:
        if char in number:
            number_satisfied += 1
        elif char in lowercase:
            lowercase_satisfied += 1
        elif char in uppercase:
            uppercase_satisfied += 1
        elif char in specialcharacter:
            special_satisfied += 1
        if number_satisfied > 0 and lowercase_satisfied > 0 and uppercase_satisfied > 0 and special_satisfied > 0:
            print('This password is valid')
            break
    if number_satisfied == 0 or lowercase_satisfied == 0 or uppercase_satisfied == 0 or special_satisfied == 0:
        print('This password is not valid')
        break
