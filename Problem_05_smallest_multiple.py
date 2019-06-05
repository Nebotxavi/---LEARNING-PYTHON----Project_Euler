"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import timeit


def smallest_multiple():
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    num = 40
    div = 0

    while div == 0:
        for i in check_list:
            if num % i == 0:
                if i == 20:
                    div = num
                    break
                else:
                    continue
            else:
                num += 20
                break

    return div

# Option 2, simple but longer execution.


def short_smallest_multiple():
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    i = 40

    while True:
        if all(i % a == 0 for a in check_list):
            return i
        else:
            i += 20


setup1 = 'from __main__ import smallest_multiple'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(smallest_multiple())", setup= setup1, number=1))}.')

setup1 = 'from __main__ import short_smallest_multiple'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(short_smallest_multiple())", setup= setup1, number=1))}.')

