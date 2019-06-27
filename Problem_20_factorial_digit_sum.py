"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import timeit


def fact_sum(n):
    total = 1
    for num in range(n, 1, -1):
        total *= num

    return sum([int(i) for i in list(str(total))])


setup1 = 'from __main__ import fact_sum'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(fact_sum(100))", setup= setup1, number=1))}.')
