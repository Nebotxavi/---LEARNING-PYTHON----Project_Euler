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
    sum_square = 0
    square_of_sum = 0

    for i in range(1, 101):
        sum_square += i ** 2
        square_of_sum += i

    return (square_of_sum ** 2) - sum_square


def sum_square_dif_short():
    seq = range(1, 101)
    sum_square = sum(i ** 2 for i in seq)
    square_of_sum = sum(seq) ** 2

    return square_of_sum - sum_square


def sum_square_dif_one_line():
    seq = range(1, 101)
    return sum(seq) ** 2 - sum(i ** 2 for i in seq)


setup1 = 'from __main__ import sum_square_dif'
setup2 = 'from __main__ import sum_square_dif_short'
setup3 = 'from __main__ import sum_square_dif_one_line'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(sum_square_dif())", setup= setup1, number=1))}.')
print(f'Execution time: ' +
      f'{(timeit.timeit("print(sum_square_dif_short())", setup= setup2, number=1))}.')
print(f'Execution time: ' +
      f'{(timeit.timeit("print(sum_square_dif_one_line())", setup= setup3, number=1))}.')
