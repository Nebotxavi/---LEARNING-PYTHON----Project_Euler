import timeit


def fib(limit):

    n1, n2, index = 0, 1, 1

    while True:
        temp = n1
        n1 = n2
        n2 = temp + n2
        index += 1
        if len(str(n2)) >= limit:
            return index


# Recursive option. It will not work unless the maximum recursion allowed is not modified.

def fib_recursive(n1=0, n2=1, index=1):
    if len(str(n2)) >= 1000:
        return index
    return fib_recursive(n2, n1 + n2, index + 1)


setup1 = 'from __main__ import fib'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(fib(1000))", setup= setup1, number=1))}.')
