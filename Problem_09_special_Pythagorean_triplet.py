"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import timeit


def triplet():
    for sec in range(2, 40):
        for first in range(15, 40):
            if sec < first:
                a= ((first ** 2) - (sec**2))
                b= 2 * first * sec
                c= ((first ** 2) + (sec**2))
                if a + b + c == 1000:
                    return f'{a}*{b}*{c}= {a*b*c}'


setup1 = 'from __main__ import triplet'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(triplet())", setup= setup1, number=1))}.')
