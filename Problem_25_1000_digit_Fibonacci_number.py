"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import timeit


def fib(limit):

    n1, n2, index = 0, 1, 1

    while True:
        temp = n1
        n1 = n2
        n2 = temp + n2
        index += 1
        if len(str(n2)) >= limit:
            return index


# Recursive option. It will not work unless the maximum recursion allowed is not modified.

def fib_recursive(n1=0, n2=1, index=1):
    if len(str(n2)) >= 1000:
        return index
    return fib_recursive(n2, n1 + n2, index + 1)


setup1 = 'from __main__ import fib'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(fib(1000))", setup= setup1, number=1))}.')
