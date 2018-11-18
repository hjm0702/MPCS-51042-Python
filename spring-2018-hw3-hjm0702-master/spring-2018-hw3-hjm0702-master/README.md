# MPCS 51042, Python Programming

**Homework 3**

**Due**: April 16 at 12:00pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1

Write a function called `vectorize(func)` that takes a function as its only positional argument and returns a new function that calls `func` multiple times. The new function should accept any number of positional arguments. If N arguments are passed to the new function, `func` is called N times with each of the values as a single argument. The new function should return a list of return values from each invocation of `func`.

To get a feel for its use, take a look at the following example:
```pycon
>>> from math import sqrt
>>> multisqrt = vectorize(sqrt)
>>> multisqrt(4.0, 25.0, 1.0, 10.0)
[2.0, 5.0, 1.0, 3.1622776601683795]
```

## Problem 2

Write a generator function that mimics the Unix `grep` command. The function definition should look like:

```python
def grep(pattern, lines, ignore_case=False):
    ...
```

`pattern` should be a string that represents a "pattern" that we want to find within each line. `lines` should be an iterable of strings (this could be a list of strings, a file object that can be iterated over, or a generator). Finally, the `ignore_case` argument indicates whether we want to search for the pattern in a case-sensitive or case-insensitive manner. To be clear, the function must `yield` values, not return a list of matching strings.

Example usage:

```pycon
>>> lines = ['I went to Poland.',
...          'He went to Spain.',
...          'She is very happy.']
>>> for line in grep('went', lines):
...     print(line)
I went to Poland.
He went to Spain.
>>> for line in grep('i', lines, ignore_case=True):
...     print(line)
I went to Poland.
He went to Spain.
She is very happy.
```

# Problem 3

For this problem, you're asked to write a program that implements methods for password cracking and allows a user to hack into password-protected .zip archives. While there are many methods for cracking passwords, you will be implementing two of the most rudimentary methods:

- **Brute-force attack**: In this method, the attacker systematically checks all possible passwords until a correct one is found. Given enough time and resources, the password is guaranteed to be found. However, if the actual password is sufficiently long, the time it will take to check all possible passwords becomes prohibitively long.
- **Dictionary attack**: In this method, the attacker uses a "dictionary" of words (for example, all words in an actual dictionary) as attempted passwords until a correct one is found. If none of the words in the dictionary results in a successful authentication, then the attack fails.

## Specifications

You have been provided with two password-protected zip files, brute_force.zip and dictionary.zip, that you are asked to crack (with the full blessing of Prof. Romano). To do so, you must write several functions that work together:

### Brute force attack

The `brute_force_attack(filename, chars, n)` function takes three positional arguments:

1. `filename` -- filename of a .zip file to crack
2. `chars` -- string containing characters to test in each position
3. `n` -- integer representing maximum password legnth to check
 
The function should open the file using the [zipfile.ZipFile](https://docs.python.org/3/library/zipfile.html#zipfile-objects) class from the standard library and attempt to extract all files using its [extractall](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall) method. Note that the `pwd` argument of `extractall` must be a bytes object rather than a string, so the password you are checking needs to be encoded. The `extractall` method should be attempted for all passwords of length 1 to `n` consisting of the characters in `chars`. For example, if `chars` is the string `'abcde'`, the function would check the passwords `a`, `b`, `c`, `d`, and `e`, then proceed to two-letter combinations `aa`, `ab`, `ac`, ..., `ee`, then three-letter combinations `aaa`, `aab`, and so on. To generate all combinations of a given length, you may find the [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product) function from the standard library to be particularly useful.

The function must handle exceptions appropriately:
- If `filename` refers to an invalid file location, `FileNotFoundError` should be raised.
- Running the `ZipFile.extractall` method with an incorrect password will result in an exception being raised. These exceptions must be caught so that the function may continue checking more passwords.
- If the password is not found after checking all passwords of length `n` or less, the function should raise a `LookupError`. If the password is found, it should simply be returned as a string.

### Dictionary attack

The `dictionary_attack(filename, dict_file, max_words=None)` accepts three positional arguments:

1. `filename` -- filename of a .zip file to crack
2. `dict_file` -- filename of a dictionary file containing common passwords
3. `max_words` -- The maximum number of passwords to attempt from the dictionary file. If `None` is passed, all words in the dictionary file should be used.

As before, the function should open the .zip file using the `zipfile.ZipFile` class. Rather than checking combinations of letters, this function should open the dictionary file and use the word on each line as an attempted password that is passed to the `ZipFile.extractall` method. Exceptions must be handled in the same manner as the `brute_force_attack` function. The return value of the function should be the password.

A download.py script is included in your repository that will automatically download a well-known dictionary file called rockyou.txt that you can use when testing this function. Note that this dictionary file uses the so-called "Latin 1" encoding and must be opened using `open(..., encoding='latin-1')`.

### Main function

In addition to the two attack functions, you must implement a `main()` function which handles user input and calls the other functions. The program flow should go as follows:

1. The user is prompted to enter a filename for the .zip file.
2. The user is prompted to select a method for password cracking (acceptable options are the strings `bruteforce` and `dictionary`).
3. If a brute-force attack was selected, the user is prompted for a maximum length. The `brute_force_attack` function is then called with `chars` being a string consisting of all lowercase letters a-z. If a password is found, it is displayed. If a password is not found, an error message should be displayed and the program terminates. If the filename was found to be invalid, the user should be prompted for a new file starting from step 1.
4. If a dictionary attack was selected, the user is prompted for the name of a dictionary file. The `dictionary_attack` function is then called. Again, if a password is found, it is displayed. If a password is not found, an error message should be displayed. If a filename was found to be invalid, the user should be prompted for a new file starting from step 1.

As in the last homework assignment, the `main()` function should be called in a block at the end of the script as follows:
```Python
if __name__ == '__main__':
    main()
```

Example sessions:
```
~ $ python problem2.py
Enter .zip file: brute_force.zip
Cracking method: bruteforce
Maximum length: 5
Password: ***

~ $ python problem2.py
Enter .zip file: dictionary.zip
Cracking method: dictionary
Enter dictionary file: rockyou.txt
Password: ************

```

## Disclaimer

This problem is meant to be educational and should not be construed as encouragement to hack into systems for which you otherwise do not have access. Breaking into secure computer systems is illegal in the US under both federal and state laws and can result in fines and imprisonment.