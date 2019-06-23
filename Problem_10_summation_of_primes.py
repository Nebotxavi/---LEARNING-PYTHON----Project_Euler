"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import timeit


def sum_primes(num):

    not_primes = set()
    primes = [2]

    for i in range(3, num + 1, 2):
        if i in not_primes:
            continue

        for ind in range(i*3, num + 1, i*2):
            not_primes.add(ind)

        primes.append(i)

    return sum(primes)


setup1 = 'from __main__ import sum_primes'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(sum_primes(2000000))", setup= setup1, number=1))}.')
