import types

def grep(pattern, lines, ignore_case = False):

    if isinstance(lines, list):
        if ignore_case == True:
            for line in lines:
                if pattern.lower() in line.lower():
                    yield line
        elif ignore_case == False:
            for line in lines:
                if pattern in line:
                    yield line

    elif isinstance(lines, types.GeneratorType):
        # print(list(lines))
        if ignore_case == True:
            for line in list(lines):
                if pattern.lower() in line.lower():
                    yield line
        elif ignore_case == False:
            for line in list(lines):
                # print(line)
                if pattern in line:
                    yield line

    else:
        f = lines.readlines()
        if ignore_case == True:
            for line in f:
                if pattern.lower() in line.lower():
                    yield line
        elif ignore_case == False:
            for line in f:
                if pattern in line:
                    yield line

if __name__ == "__main__":
    lines1 = ['I went to Poland.',
    'He went to Spain.',
    'She is very happy.']

    lines2 = open('text.txt',"r", encoding='utf8')


    print ("\n[Input : A list of strings]")
    for x in list(grep("i", lines1, ignore_case=True)):
        print (x)
    print ("-----------------")
    for x in list(grep("went", lines1)):
        print (x)

    print ("-----------------")

    print ("\n[Input : A file]")
    for x in list(grep("went", lines2)):
        print (x)
    lines2.close()

    lines2 = open('text.txt',"r", encoding='utf8')
    print ("-----------------")
    for x in list(grep("i", lines2, ignore_case=True)):
        print (x)
    lines2.close()

    lines4 = (c*3 for c in 'pyithon')

    print ("\n[Input : A generator]")
    for x in list(grep("went", lines4)):
        print (x)

    lines3 = (c*3 for c in 'pyithon')

    print ("-----------------")
    for x in list(grep("i", lines3, ignore_case=True)):
        print (x)
