
def userinput():
    '''Prompt user to input two list'''
    first = input("Enter list 1: ")
    second = input("Enter list 2: ")
    first_strip = first.split(",")
    second_strip = second.split(",")
    x = [first_strip, second_strip]
    return x

def dup_finder(list):
    '''Find duplicated numbers'''
    answer = []
    for first_number in list[0]:
        if "2" in first_number:
            for second_number in list[1]:
                if int(first_number) == int(second_number):
                    answer.append(int(first_number))
    return answer

if __name__ == "__main__":
    print(dup_finder(userinput()))
