"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import timeit


def sum_square_dif():
    seq = range(1, 101)
    sum_square = sum(i ** 2 for i in seq)
    square_of_sum = sum(seq) ** 2

    return square_of_sum - sum_square


setup1 = 'from __main__ import sum_square_dif'

print(f'Execution time: ' +
      f'{(timeit.timeit("(sum_square_dif())", setup= setup1, number=20)/20)}.')
