# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# An anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once. Spaces and punctuation 
# are not taken into consideration. 
# You should write two functions. The first one called check_anagrams takes two parameters 
# (strings) checks whether the two string are anagrams of each other. check_anagrams 
# returns True if the two strings are anagrams and False otherwise. The main function 
# should ask the user to enter two strings and prints the result by calling the other 
# function check_anagrams.

# USE OF LIST, such as sorted(), split(), etc, and OTHER CONCEPTS
# THAT ARE NOT COVERED YET ARE FORBIDDEN.
# YOU WILL NOT GET CREDIT BY DOING SO.


def check_anagrams(S1, S2):
    # WRITE YOUR CODE HERE
    S1_alpha, S2_alpha = '', ''
    for i in S1:
        if i.isalpha():
            S1_alpha += i
    for j in S2:
        if j.isalpha():
            S2_alpha += j
    S1_space, S2_space = S1_alpha.lower(), S2_alpha.lower()
    for a in S1_alpha.lower():
        S2_space = S2_space.replace(a,' ')
    for b in S2_alpha.lower():
        S1_space = S1_space.replace(b,' ')
    return S2_space.isspace() and S1_space.isspace()


def main():
    S1 = input('Enter the first word or phrase:\n')
    S2 = input('Enter the second word or phrase:\n')
    if check_anagrams(S1, S2):
        print('"{0}", and "{1}" are anagrams.'.format(S1, S2))
    else:
        print('"{0}", and "{1}" are not anagrams.'.format(S1, S2))


# Call the main() function, DO NOT change the code below.
if __name__ == '__main__':
    main()
