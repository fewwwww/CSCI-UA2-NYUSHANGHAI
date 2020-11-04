# PROGRAMMING ASSIGNMENT 05
# Filename: 'exercise2.py'
#
# Write the code for function find_character.
# The function find_character:
#   • takes two parameters aString (type str) and aChar (type str)
#   • returns the index of first occurrence of the specified character;
#   • returns -1 if the character is not found

def main():
    #calling the function
    a = find_character("hello world", "o") #also catch the returned value
    print(a) #print the returned value

    #empty line
    print()

    a = find_character("hello world", "p") #also catch the returned value
    print(a) #print the returned value


def find_character(aString, aChar):
    #WRITE YOUR CODE HERE, remember to delete the pass
    count = 0
    for character in aString:
        if character == aChar:
            return count
        else:
            count += 1
    return -1



#Call the main() function, DO NOT change the code below
if __name__ == '__main__':
    main()



