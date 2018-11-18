import re
from collections import defaultdict
from functools import reduce

def fill_completions(fd):
    '''Generating a completion dictionary'''
    f = open(fd, 'r', encoding='UTF8')
    clean_list = []
    lst = [line.strip().split() for line in f.readlines()]
    for line in lst:
        for word in line:
            if not re.search('\d', word) and not re.search('\W',word) and len(word) > 1:
                clean_list.append(word.lower())

    final_list = list(set(clean_list))
    c_dict = defaultdict(list)
    for word in final_list:
        for i in range(len(word)):
            c_dict[i, word[i]].append(word)

    return c_dict

def find_completions(prefix, c_dict):
    '''find words from the dictinary'''
    empty_list = []
    for i in range(len(prefix)):
        empty_list.append(c_dict[i, prefix[i]])

    final_list = []
    for lst in empty_list:
        for word in lst:
            if word not in final_list:
                final_list.append(word)

    return list(reduce(set.intersection, [set(item) for item in empty_list]))

if __name__ == "__main__":
    openfile = "articles.txt"
    final_dict = fill_completions(openfile)
    finish = False
    while not finish:
        userinput = input("Enter Prefix:")

        if userinput == "(quit)":
            finish = True
        else:
            if len(find_completions(userinput.lower(),final_dict)) > 0:
                for i in find_completions(userinput.lower(),final_dict):
                    print ('  '+i)
            else:
                print ("No completions")
