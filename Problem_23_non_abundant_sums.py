"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math
import timeit


def get_sum_divisors(n):
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.update([int(n / i), i])

    divs.remove(n)
    return sum(divs)


def sum_non_abundant_nums():
    non_abundant = set()
    abundant = set()

    for i in range(1, 28123):
        if get_sum_divisors(i) > i:
            abundant.add(i)
        if not any((i - abn in abundant) for abn in abundant):
            non_abundant.add(i)

    return sum(non_abundant)


setup1 = 'from __main__ import sum_non_abundant_nums'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(sum_non_abundant_nums())", setup= setup1, number=1))}.')
