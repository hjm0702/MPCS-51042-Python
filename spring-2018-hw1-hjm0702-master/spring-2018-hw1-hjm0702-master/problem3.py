def userinput():
    '''Handling User input'''
    list = input("Enter numbers: ")
    split_input = list.split()

    final_input = []
    for number in split_input:
        if "e" in number:
            raw_number = number.split("e")
            final_number = float(float(raw_number[0])*10**float(raw_number[-1]))
            final_input.append(final_number)
        else:
            final_input.append(float(number))

    return final_input

def scm(list):
    '''Calculate sample central moment'''
    r = input("Enter r:")
    if r.isdigit() > 0:
        average = sum(list)/len(list)
        final = 0
        for number in list:
            final = final+(number-average)**int(r)
        return (final/len(list))
    else:
        return "r must be a positive integer"

if __name__ == "__main__":
    print (scm(userinput()))
