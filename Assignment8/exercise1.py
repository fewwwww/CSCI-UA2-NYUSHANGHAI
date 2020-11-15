# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    - it inserts all the content from file2.txt to the beginning of file1.txt
    
    Note: After execution of the your program, only file1.txt is updated, file2.txt does not change."""
    #WRITE YOUR PROGRAM HERE
    file1 = open('file1.txt', 'r')
    file1_data = file1.read()
    file1.close()
    file2_r = open('file2.txt', 'r')
    file2_data = file2_r.read()
    file2_r.close()
    file1_w = open('file1.txt', 'a')
    file1_w.write(file2_data + file1_data)
    file1_w.close()
    

#Call the main() function
if __name__ == '__main__':
    main()
