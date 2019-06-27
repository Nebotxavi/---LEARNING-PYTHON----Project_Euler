import timeit


def collatz_call(seq_amount):

    def collatz_max_seq(num):

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
        result = collatz_max_seq(i)
        if result > max_seq:
            max_seq = result
            max_num = i

    return f"{max_num} with {max_seq} sequences."


setup1 = 'from __main__ import collatz_call'

print(f'Execution time: ' +
      f'{(timeit.timeit("print(collatz_call(1000000))", setup= setup1, number=1))}.')
