"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import timeit


def prime_factor():
    num = 600851475143

    while num > 1:
        if num % 2 == 0:
            num = num // 2

        else:
            for i in range(3, num + 1, 2):
                if num % i == 0:
                    num = num // i
                    break
    
    return i 


setup1 = 'from __main__ import prime_factor'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(prime_factor())", setup= setup1, number=1))}.')
