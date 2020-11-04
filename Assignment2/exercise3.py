# PROGRAMMING ASSIGNMENT 02
# Filename: 'exercise3.py'
#
# Write a program that does the following (in the specified order):
# 1. asks the user to input a year (type: int)
# 2. prints the message "Leap year" or "Not leap year" on a first line
# 3. then, only if applicable, prints the message "World Cup year" or "Euro Cup year" on a second line
#
# WRITE YOUR CODE AFTER THIS LINE
year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")
if (year - 1950) % 4 == 0 and year > 1950:
    print("World Cup Year")
if ((year - 1960) % 4 == 0 or year == 2021) and year > 1960 and year != 2020:
    print("Euro Cup Year")