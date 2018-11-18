
def accept(*args):
    for arg in args:
        if not isinstance(arg,type):
            raise TypeError(f'\'{arg}\' is not a type object.')
    def decorator(func):
        def inner(*args2):
            for index, arg2 in enumerate(args2):
                if not isinstance(arg2, args[index]):
                    raise TypeError(f'Argument 0 of {func.__name__} is not a {args[index].__name__}')
            return func(*args2)
        return inner
    return decorator

@accept(str, int, float)
def multiply_string(s, n, x):
    return s*n,x

print(multiply_string("jon", 3,3))
