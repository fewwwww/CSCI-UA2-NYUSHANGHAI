# PROGRAMMING ASSIGNMENT 09
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def build_attraction_dict(str):
    # write your code here for Task 1
    file = open(str, 'r')
    data = file.read().strip()
    lst = data.split('\n')
    for i in range(len(lst)):
        lst[i] = lst[i].split(',')
    dict = {}
    for j in range(len(lst)):
        dict[lst[j][1]] = lst[j][0]
    return(dict)


def add_attraction(dict):
    # write your code here for Task 2
    name = input('Input a new attraction: ')
    province = input('Input the province: ')
    dict[name] = province


def build_provinse_attraction_dict(dict):
    # write your code here for Task 3
    dict_new = {}
    for key, value in dict.items():
        if value not in dict_new.keys():
            dict_new[value] = [key]
            continue
        dict_new[value].append(key)
    return dict_new


def most_attractions(dict):
    # write your code here for Task 4
    result = set()
    for key, value in dict.items():
        if len(value) >= 3:
            result.add(key)
    return result


def main():
    # write your code here for Task 5
    dict = build_attraction_dict('top_tourist_attractions.txt')
    add_attraction(dict)
    dict_new = build_province_attraction_dict(dict)
    result = most_attractions(dict_new)
    print()
    print('Provinces with at least 3 attractions:')
    for i in result:
        print(i)


##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
