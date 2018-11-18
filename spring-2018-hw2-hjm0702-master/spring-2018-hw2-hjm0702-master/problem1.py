import csv
from datetime import datetime

def convertdate(dateinput):
    '''convert text into date format'''
    result = datetime.strptime(dateinput, '%m/%d/%Y')
    return result

def indebted():
    '''make a dictionary with date + total amount'''
    with open("indebtedness.csv", newline="") as csvfile:
        f = csv.reader(csvfile)
        final = {}
        for row in f:
            if "$" in row[-1]:
                converted_date = convertdate(row[0])
                if converted_date in final:
                    final[converted_date] = final[converted_date]+float(row[-1][1:])
                else:
                    final[converted_date] = float(row[-1][1:])

    return final

def makelist(dictionary):
    '''make sorted list for printing'''
    final = []
    for line in dictionary:
        final.append([line, dictionary[line]])

    return sorted(final)

if __name__=="__main__":
    for line in makelist(indebted()):
        print (datetime.strftime(line[0], "%m/%d/%y"),":", format(int(line[-1]),",d"))
