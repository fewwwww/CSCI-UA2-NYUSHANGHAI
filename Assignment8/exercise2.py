# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise2.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    1) asks the user to input a filename (supposedly in the same folder as this program)
	2) reads the numbers (type int) in the file (filename given by the user in previous step) and stores them into a list
	3) prints the minimum, the maximum and the average of the numbers (2 decimal places for the average)
    
    Note: your program should be impossible to crash. Think about all the possibilities to make your program crash.
    If one of the steps throws an exception, display a message to the user and your program should loop back to step 1."""
    #WRITE YOUR PROGRAM HERE
    while True:
        filename = input('Filename:\n')
        try:
            file = open(filename,'r')
        except:
           print('File not found')
        else:
            data = file.read()
            lst = data.split()
            lst_corrected = []
            for i in range(len(lst)):
                try:
                    lst[i] = int(lst[i])
                    lst_corrected.append(lst[i])
                except:
                    continue
            try:
                print('Minimum: {0}\nMaximum: {1}\nAverage: {2:.2f}'.format(min(lst_corrected),max(lst_corrected),sum(lst_corrected)/len(lst_corrected)))
                break
            except:
                print('File is empty')
                continue
    

#Call the main() function
if __name__ == '__main__':
    main()
