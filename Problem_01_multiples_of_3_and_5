#!/usr/bin/env python3
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""
import timeit

# Option 1: iterative loop


def mult_sum(n1, n2, limit=1000):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Option 2: generator expression


def mult_sum_comp(n1, n2, limit=1000):
    return sum(x for x in range(limit) if x % n1 == 0 or x % n2 == 0)


setup1 = 'from __main__ import mult_sum'
setup2 = 'from __main__ import mult_sum_comp'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(mult_sum(3, 5))", setup= setup1, number=1))}.')
print(f'Execution time: ' +
      f'{(timeit.timeit("print(mult_sum_comp(3, 5))", setup= setup2, number=1))}.')
