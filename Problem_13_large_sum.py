"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
* See
"""
import timeit


def process_file(path):
    with open(path, mode='r') as op:
        numbers_lines = op.readlines()
        numbers = (int(numbers_lines[i]) for i in range(len(numbers_lines)))
    return numbers


def large_sum(file):
    numbers = process_file(file)
    total = str(sum(numbers))
    return total[:10]


print(f'Execution time: ' +
      f'{(timeit.timeit(print(large_sum("files/problem_13.txt")), setup= setup1, number=1))}.')
