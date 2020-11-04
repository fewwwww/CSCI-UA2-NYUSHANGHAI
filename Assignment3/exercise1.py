# PROGRAMMING ASSIGNMENT 03
# Filename: 'exercise1.py'
#
# Write a program that does the following:
# • continuously asks the user to input a score which is an integer between 0 and 100 (inclusive)...
# • ...until the user enters a correct number (display a message if the user did not enter a correct number)
# • then finally prints the corresponding grade
#
# see the TABLE OF CORRESPONDENCES SCORE/GRADE in the pdf file
#
# WRITE YOUR CODE AFTER THIS LINE
while True:
    score = int(input('Score: '))
    if not 0<=score<=100:
        print('Invalid input. Please enter a score between 0 and 100.')
    elif score >= 96:
        print('Your grade is A+')
        break
    elif score >= 92:
        print('Your grade is A')
        break
    elif score >= 88:
        print('Your grade is A-')
        break
    elif score >= 84:
        print('Your grade is B+')
        break
    elif score >= 81:
        print('Your grade is B')
        break
    elif score >= 78:
        print('Your grade is B-')
        break
    elif score >= 75:
        print('Your grade is C+')
        break
    elif score >= 72:
        print('Your grade is C')
        break
    elif score >= 69:
        print('Your grade is C-')
        break
    elif score >= 66:
        print('Your grade is D+')
        break
    elif score >= 63:
        print('Your grade is D')
        break
    else:
        print('Your grade is F')
        break