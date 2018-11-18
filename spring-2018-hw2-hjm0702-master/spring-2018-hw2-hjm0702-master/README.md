# MPCS 51042, Python Programming

**Homework 2**

**Due**: April 9 at 12:00pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1

A 2014 article in the [Chicago Tribune](http://articles.chicagotribune.com/2014-02-20/news/ct-emanuel-city-employee-scofflaws-met-20140220_1_city-workers-chicago-public-city-employee-debt) highlighted how Chicago mayor Rahm Emanuel indicated to city employees that they must pay any outstanding debt to the city (parking tickets, water bills, etc.) or face possible suspension/firing. In this problem, you will assess how successful (or not) mayor Emanuel has been in getting city employees to pay outstanding debt by analyzing [open data](https://data.cityofchicago.org/) provided by the City of Chicago.

You are provided a comma-separated value file `indebtedness.csv` that contains information on the total debt owed by employees of various departments listed by date. Your task is to write a program that displays the total amount of debt owed by city employees for each date shown in the csv file. The output must be sorted by date, starting from the oldest entries (`10/14/2011`) and continuing to the present. The total amount owed should be displayed rounded to the nearest dollar with thousands separated by commas.

Although we have not covered them yet, you are allowed to use the [csv](https://docs.python.org/3/library/csv.html) and [datetime](https://docs.python.org/3/library/datetime.html) standard library modules if you wish.

Sample output:
```
10/14/2011: 2,553,610
10/21/2011: 2,326,302
10/28/2011: 2,132,597
11/04/2011: 1,950,591
11/11/2011: 1,810,242
...
```

## Problem 2

Write a function that joins together single components of a path to produce a
full path with directories separate by slashes. For example, it should operate
in the following manner:
```pycon
>>> full_paths(['usr', ['lib', 'bin'], 'config', ['x', 'y', 'z']])
['/usr/lib/config/x',
 '/usr/lib/config/y',
 '/usr/lib/config/z',
 '/usr/bin/config/x',
 '/usr/bin/config/y',
 '/usr/bin/config/z']
>>> full_paths(['codes', ['python', 'c', 'c++'], ['Makefile']], base_path='/home/user/')
['/home/user/codes/python/Makefile',
 '/home/user/codes/c/Makefile',
 '/home/user/codes/c++/Makefile']
```

The function definition should look as follows:

```python
def full_paths(path_components, base_path='/'):
    ...
```

The `path_components` argument accepts an iterable in which each item is either a list of strings or a single string. Each item in `path_components` represents a level in the directory hierarchy. The function should return every combination of items from each level. With the `path_components` list, a string and a list containing a single string should produce equivalent results as the second example above demonstrates. The `base_path` argument is a prefix that is added to every string that is returned. The function should return a list of all the path combinations (a list of strings).

If you need to check whether a variable is iterable, the "Pythonic" way to do this is

```python
from collections.abc import Iterable

if isinstance(x, Iterable):
    ...
```

However, note that strings are iterable too!

You are allowed to use functionality from the standard library for this problem.

## Problem 3

Nowadays we take word completion for granted. Our phones, text editors, and word processing programs all give us suggestions for how to complete words as we type based on the letters typed so far. These hints help speed up user input and eliminate common typographical mistakes (but can also be frustrating when the tool insists on completing a word that you don’t want completed).

You will implement two functions that such tools might use to provide command completion. The first function, `fill_competions`, will construct a dictionary designed to permit easy calculation of possible word completions. A problem for any such function is what vocabulary, or set of words, to allow completion on. Because the vocabulary you want may depend on the domain a tool is used in, you will provide `fill_competions` with a representative sample of documents from which it will build the completions dictionary. The second function, `find_completions`, will return the set of possible completions for a start of any word in the vocabulary (or the empty set if there are none). In addition to these two functions, you will implement a simple main program to use for testing your functions.

## Specifications

- `fill_completions(fd)` returns a dictionary. This function takes as input an opened file. It loops through each line in the file, splitting the lines into individual words (separated by whitespace) and builds a dictionary:

  - The keys of the dictionary are tuples of the form `(n, l)` for a non-negative integer `n` and a lowercase letter `l`.
  - The value associated with key `(n, l)` is the set of words in the file that contain the letter `l` at position `n`. For simplicity, all vocabulary words are converted to lower case. For example, if the file contains the word "Python" and `c_dict` is the returned dictionary, then the sets `c_dict[0, "p"]`, `c_dict[1, "y"]`, `c_dict[2, "t"]`, `c_dict[3, "h"]`, `c_dict[4, "o"]`, and `c_dict[5, "n"]` all contain the word `"python"`.
  - Words are stripped of leading and trailing punctuation.
  - Words containing non-alphabetic characters are ignored, as are words of length 1 (since there is no reason to complete the latter).

- `find_completions(prefix, c_dict)` returns a set of strings. This function takes a prefix of a vocabulary word and a completions dictionary of the form described above. It returns the set of vocabulary words in the completions dictionary, if any, that complete the prefix. It the prefix cannot be completed to any vocabulary words, the function returns an empty set.

- `main()`, the test driver:

  - Opens the file named `articles.txt`. This file contains the text of recent articles pulled from BBC.
  - Calls `fill_competions` to fill out a completions dictionary using this file.
  - Repeatedly prompts the user for a prefix to complete.
  - Prints each word from the set of words that can complete the given prefix (one per line). If no completions are possible, it should just print "No completions".
  - Quit if the user enters the word "\<quit\>".

- To call the `main()` function, put a block at the end of your script with the follow lines (we will discuss this technique later on in the class). This allows your script to run when executed from a command line.
    ```python
    if __name__ == '__main__':
        main()
    ```

## Example session

```
$ python problem3.py
Enter prefix: za
  zara
  zakharova
  zapad
Enter prefix: lum
  lumley
  lump
  lumet
Enter prefix: multis
  No completions
Enter prefix: <quit>
```
