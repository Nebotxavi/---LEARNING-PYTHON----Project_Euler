"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""

import timeit

# Option 1: Simple version


def power_digit_sum(n=2, p=1000):
    num = n ** p
    nums = (list(str(num)))
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return sum(nums)


# Option 2: Generator comprehension


def power_digit_sum2(n=2, p=1000):
    num = n ** p
    return sum(int(i) for i in str(num))


setup1 = 'from __main__ import power_digit_sum'
setup2 = 'from __main__ import power_digit_sum2'


print(f'Execution time: ' +
      f'{(timeit.timeit("print(power_digit_sum(2, 1000))", setup= setup1, number=1))}.')
print(f'Execution time: ' +
      f'{(timeit.timeit("print(power_digit_sum2(2, 1000))", setup= setup2, number=1))}.')
