# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise2.py'
#
# Titles of books or articles generally capitalize the first letter of every important 
# word.  The first word is always capitalized. The following words should not be 
# capitalized: a, an, the, at, by, for, in, of, on, to, up, and, as, but, or, and nor.
#You must write a function named title_case that capitalizes the appropriate characters 
# in a string. Include a main program that reads a string from the user, capitalizes it 
# using your function, and displays the result. Assume user will always input in lower cases
# with no punctuation.

# USE OF LIST FUNCTIONS ARE PROHIBITED.
# YOU WILL NOT GET CREDIT BY DOING SO.

    

def title_case(title):
    #WRITE YOUR CODE HERE
    nocap = 'aantheatbyforinofontoupandasbutornor'
    index_0 = 0
    index_1 = 0
    formatted_title = ''
    for char in title:
        index_1 += 1
        if char.isspace():
            word = title[index_0:index_1]
            index_0 = index_1
            if word[:-1] in nocap:
                formatted_title += word
            else:
                word = word[0].capitalize()+word[1:]
                formatted_title += word

    last_word = title[index_0:]
    if last_word in nocap:
        formatted_title += last_word
    else:
        last_word = last_word[0].capitalize() + last_word[1:]
        formatted_title += last_word

    formatted_title = formatted_title[0].capitalize() + formatted_title[1:]

    return formatted_title


def main():
    title = input('Enter a title to be formatted:\n')
    print('Here is your title:  {}'.format(title_case(title)))
#Call the main() function, DO NOT change the code below.
if __name__ == '__main__':
    main()
