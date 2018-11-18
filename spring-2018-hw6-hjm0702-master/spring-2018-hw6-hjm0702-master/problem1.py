
def maketuple(func):
    def inner(*args, **kwargs):
        try :
            answer = [x for x in func(*args, **kwargs)]
            return tuple(answer)
        except TypeError:
            return (func(*args),)
    return inner


@maketuple
def uppercase(s):
    return s.upper()
print(uppercase('Java'))

@maketuple
def sum(a, b):
    return a + b
print(sum(1, 2))
