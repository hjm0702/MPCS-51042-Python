# import re

def userinput():
    '''Ask user to input a comman-seperated integers'''
    list = input("Enter integers: ")
    sorted_list = list.split(",")
    return sorted_list

def generator(list):
    '''Generate a list of integers'''
    wip = []
    for number in list:
        if "-" in number:
            split_number = number.split("-")
            if int(split_number[-1]) >= int(split_number[0]):
                x = 0
                while x <= int(split_number[-1])-int(split_number[0]):
                    wip.append(int(split_number[0])+x)
                    x = x+1
            elif int(split_number[-1]) < int(split_number[0]):
                return ""
        elif number.isdigit():
            wip.append(int(number))

    return set(sorted(wip))

if __name__ == "__main__":
    answer = generator(userinput())
    if answer == "":
        print("Please check your input.")
    else:
        print(list(answer))
