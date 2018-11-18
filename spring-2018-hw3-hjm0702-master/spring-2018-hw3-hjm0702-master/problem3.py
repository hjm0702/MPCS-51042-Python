from zipfile import ZipFile
from itertools import product
# from itertools import permutations

def brute_force_attack(filename, chars, n):
    f = ZipFile(filename, 'r')
    for i in range(n+1)[1:]:
        pwdlist = list(product(chars,repeat = i))
        for word in pwdlist:
            word1 = str.encode("".join(word))
            try:
                extract = ZipFile.extractall(f, pwd=word1)
                print ("Password:", "".join(word))
                break
            except RuntimeError:
                pass

    raise LookupError

def dictionary_attack(filename, dict_file, max_words):
    f = ZipFile(filename, 'r')
    dictfile = open(dict_file, encoding='latin-1')
    filereader = dictfile.readlines()

    if max_words == "":
        for item in filereader:
            try :
                word1 = str.encode(item[:-1])
                extract = ZipFile.extractall(f, pwd=word1)
                print ("Password:", item[:-1])
                break
            except RuntimeError:
                pass
        raise LookupError
    else:
        max_reader = filereader[:int(max_words)]
        for item in max_reader:
            try :
                word1 = str.encode(item[:-1])
                extract = ZipFile.extractall(f, pwd=word1)
                print ("Password:", item[:-1])
                break
            except RuntimeError:
                pass
        raise LookupError

def main():
    file_check = False
    while not file_check:
        file_input = input("Enter .zip file: ")
        try :
            f = ZipFile(file_input, 'r')
            method_input = input("Craking method: ")
            if method_input == "bruteforce":
                length_input = int(input ("Maximum length: "))
                password = input("Password: ")

                brute_force_attack(file_input, password, length_input)
                file_check = True
            elif method_input == "dictionary":
                dict_input = input("Enter dictionary file: ")
                max_words_input = (input("Enter max words: "))
                dictionary_attack(file_input, dict_input, max_words_input)
                file_check = True

        except FileNotFoundError:
            print("File Nof Found")

if __name__ == "__main__":
    main()
