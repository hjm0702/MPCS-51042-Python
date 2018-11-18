''''
from math import sqrt
multisqrt = vectorize(sqrt)
multisqrt(4.0, 25.0, 1.0, 10.0)
[2.0, 5.0, 1.0, 3.1622776601683795]
'''
from math import sqrt

def vectorize(func):
    def inner(*args):
        return [func(x) for x in args]
    return inner

if __name__ == "__main__":

    multisqrt = vectorize(sqrt)
    print (multisqrt(4.0, 25.0, 1.0, 10.0))
