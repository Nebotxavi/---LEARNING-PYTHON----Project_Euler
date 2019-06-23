"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import timeit


def st_prime(limit):
    not_prime = set()
    primes = [2]

    for i in range(3, limit, 2):
        if i in not_prime:
            continue

        for ind in range(i * 3, limit, i * 2):
            not_prime.add(ind)

        primes.append(i)

        if len(primes) == 10001:
            return primes[10000]


setup1 = 'from __main__ import st_prime'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(st_prime(10001))", setup= setup1, number=1))}.')
