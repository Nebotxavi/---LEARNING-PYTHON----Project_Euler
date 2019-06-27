"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import timeit
import math


def sum_divisors(n):
    """ Sum all the divisors excluding the given parameter."""
    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                divs.append(i)
            else:
                divs.extend([int(n / i), i])

    divs.remove(n)
    return sum(divs)


def amicable(limit=10000):
    amicable_nums = []
    for i in range(2, limit + 1):
        if i in amicable_nums:
            continue
        else:
            dn1 = sum_divisors(i)
            dn2 = sum_divisors(dn1)
            if i == dn2 and i != dn1:
                amicable_nums.extend([i, dn1])

    return sum(amicable_nums)


setup1 = 'from __main__ import amicable'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(amicable())", setup= setup1, number=1))}.')
