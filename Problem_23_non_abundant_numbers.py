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
