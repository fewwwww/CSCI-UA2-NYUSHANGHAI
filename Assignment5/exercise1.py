# PROGRAMMING ASSIGNMENT 05
# Filename: 'exercise1.py'
#
# Write the code for function diamond.
# The function diamond:
#   • takes one parameter N (type int), its value must be odd and in the range [3, 99]
#   • it draws a square shape made of integer values and spaces:
#       - integer values are always printed with 2 digits (for example, value 7 is printed 07)
#       - every line consists of integer values from 1 up to N , where some values have to be
#       replaced by spaces instead
#       - the first and last row are full (no space)
#       - the middle row is empty except for values 1 and N ,
#       - each row from the FIrst one to the middle one is increasingly empty from its center
#       - each row from the middle one to the last one is increasingly full to its center

def main():
    #try to draw some diamonds by calling the function diamond
    print('Calling: diamond(5)')
    diamond(5)
    
    #empty line
    print()
    
    print('Calling: diamond(15)')
    diamond(15)


def diamond(N):
    #write your code here, remember to delete the pass
    nums = ''
    for i in range(1,N+1):
        if i < 10:
            new_num = '0{0}'.format(i)
            nums += new_num
        else:
            new_num = '{0}'.format(i)
            nums += new_num

    length = len(nums)
    blank = ' '
    line_front_index = length//2+1
    line_lat_index = length//2-1
    print(nums)
    for line in range(1,N//2):
        step = line*2
        blank_num = line*4 - 2
        print(nums[:line_front_index-step]+blank_num*blank+nums[line_lat_index+step:])
    print(nums[:2]+(length-4)*blank+nums[-2:])
    for line in range(N//2-1,0,-1):
        step = line * 2
        blank_num = line * 4 - 2
        print(nums[:line_front_index-step]+blank_num*blank+nums[line_lat_index+step:])
    print(nums)


#Call the main() function, DO NOT change the code below
if __name__ == '__main__':
    main()
