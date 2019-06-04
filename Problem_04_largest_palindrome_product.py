"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import timeit


def palindrome(product):
    if product == product[::-1]:
        return True
    else:
        return False


def palindrome_product():
    palindromes = []
    for ind in range(999, 100, -1):
        for i in range(999, 990, -1):
            product = ind * i
            if palindrome(str(product)):
                palindromes.append(product)

    return max(palindromes)


setup1 = 'from __main__ import palindrome_product'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(palindrome_product())", setup= setup1, number=1))}.')
