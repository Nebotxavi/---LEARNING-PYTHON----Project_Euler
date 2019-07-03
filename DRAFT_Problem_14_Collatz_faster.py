"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import timeit


def collatz_max_seq(seq_amount=1000000):

    def get_seq(num):

        temp_num = num
        count = 0

        while temp_num > 1:

            if temp_num % 2 == 0:
                temp_num //= 2
            else:
                temp_num = temp_num * 3 + 1

            if temp_num in num_seq:
                count += num_seq[temp_num]
                break
            else:
                count += 1

        num_seq[num] = count
        return count

    num_seq = {}
    max_num = 0
    max_seq = 0

    for i in range(2, seq_amount + 1):
        seq = get_seq(i)
        if seq > max_seq:
            max_seq = seq
            max_num = i

    return max_num


setup1 = 'from __main__ import collatz_call'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(collatz_call())", setup= setup1, number=1))}.')
