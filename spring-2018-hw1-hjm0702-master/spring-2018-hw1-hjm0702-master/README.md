# MPCS 51042, Python Programming

**Homework 1**

**Due**: April 1 at 11:59pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Setup

Sign up for an account on GitHub if you haven't already and send your username to Paul on Slack.

Install Python 3 on your computer. It is highly recommended to install Python 3.6 if possible and to use a complete distribution like [Anaconda](https://www.anaconda.com/distribution/) that includes third-party packages. Write a program that prints "Hello, world!" and confirm that you can run the program from a command line. It is not necessary to submit your hello world program (if you were able to complete the actual problems, we will assume you successfully installed Python!).

To submit your assignment, you will need to have git installed on your computer. On Linux, git can easily be installed via your distribution's package manager (apt, yum, etc.). On macOS, git is installed as part of the Xcode Command Line Tools (if you want a more up-to-date version, binaries are available from git-scm.com). On Windows, we recommend installing the full version of [cmder](http://cmder.net/) which includes git-for-windows. On macOS and Windows, [GitHub Desktop](https://desktop.github.com/) makes working with repositories on GitHub especially easy.

## Problem 1

Write a program that asks the user for two lists of integers separated by commas and prints out a list of integers that appear in both lists and have the digit 2 in them. There should be no duplicates in the output list. Make sure the program works when the lists have different lengths.

Sample input/output:

```
Enter list 1: 3, 10, 12, -4, 20, 1000
Enter list 2: 12, 6, 3, 20, 4, 0, 10
[12, 20]
```

## Problem 2

Write a program that asks the user for a comma-separated list of integers or integer ranges, and prints out a sorted list of all the integers with the ranges expanded into individual integers. You can assume that all the integers entered as input are positive.

Sample input/output:

```
Enter integers: 1-4,7,3-5,10,12-14
[1, 2, 3, 4, 5, 7, 10, 12, 13, 14]
```

## Problem 3

Write a program that asks the user to input a whitespace separated list of numbers (integers or floats) and separately an integer `r` and writes out the `r`-th [sample central moment](http://mathworld.wolfram.com/SampleCentralMoment.html) of the numbers. Given a set of numbers <img src="http://latex2png.com/output//latex_a3e193ded50263c7ba1f2d27c8e8f3ec.png" width="100">, the `r`-th sample central moment is defined as

<img src="http://latex2png.com/output//latex_a6a38265f5976d7ff6c8969e1f893948.png" width="200">

where <img src="http://latex2png.com/output//latex_be095ac9593365be47bb40c058d3c031.png" width="10"> is the sample mean, defined as

<img src="http://latex2png.com/output//latex_2a0ab21f8500874baa6c73562bc3ae79.png" width="130">

You are not allowed to use any standard-library or third-party packages that perform these calculations automatically.

Sample input/output:

```
Enter numbers: 1 2 10 12 3.0 1.2e1
Enter r: 2
The rth sample central moment is 22.555555555555557.
```

HINT: The built-in [sum()](https://docs.python.org/3/library/functions.html#sum) function returns the sum of values in an iterable (such as a list).

## Problem 4

What digits (1 through 9) can replace the letters P and E such that the following equation is true?

PEEP = (PP)<sup>E</sup>

For example, if P is 2 and E is 3, the equation would be:

2332 ≠ (22)<sup>3</sup> = 10648

so 2 and 3 are clearly not a solution. Rather than solving this problem with your raw brainpower, write a program that checks each combination of digits and prints out the equation if it is satisfied.

Sample output (where P and E have been replaced by digits):

```
PEEP = (PP)^E
...
```
