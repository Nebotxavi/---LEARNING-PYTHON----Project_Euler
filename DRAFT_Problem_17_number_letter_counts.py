'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''
import timeit

def number_letter_counts(limit=1000):

    total = 0

    counting = {1:3,
                2:3,
                3:5,
                4:4,
                5:4,
                6:3,
                7:5,
                8:5,
                9:4,
                10:3,
                11:6,
                12:6,
                13:8,
                15:7,
                18:8,
                20:6,
                30:6,
                40:5,
                50:5,
                80:6
                }

    for i in range(1, limit + 1):

        if i in counting:
            total += counting[i]

        elif i < 20:
            unit = int(str(i)[-1])
            total += counting[unit] + 4
            counting[i] = counting[unit] + 4

        elif len(str(i)) == 2 and str(i).endswith('0'):
            tens = int(str(i)[0])
            total += counting[tens] + 2
            counting[i] = counting[tens] + 2

        elif len(str(i)) == 2 and (i in range(21, 60) or i in range(81, 90)):
            tens = int(str(i)[0] + '0')
            unit = int(str(i)[-1])
            total += counting[tens] + counting[unit]
            counting[i] = counting[tens] + counting[unit]

        elif len(str(i)) == 2:
            tens = int(str(i)[0])
            unit = int(str(i)[-1])
            total += (counting[tens] + 2) + (counting[unit])
            counting[i] = (counting[tens] + 2) + (counting[unit])

        elif len(str(i)) == 3 and str(i).endswith('00'):
            hundreds = int(str(i)[0])
            total += (counting[hundreds] + 7)
            counting[i] = (counting[hundreds] +7)

        elif len(str(i)) == 3:
            hundreds = int(str(i)[0])
            if int(str(i)[-2]) == 0:
                tens_units = int(str(i)[-1])
            else:
                tens_units = int(str(i)[-2:])
            total += (counting[hundreds] + 7 + 3) + counting[tens_units]
            counting[i] = (counting[hundreds] + 7 + 3) + counting[tens_units]

        elif len(str(i)) == 4 and str(i).endswith('000'):
            thousands = int(str(i)[0])
            total += counting[thousands] + 8
            counting[i] = counting[thousands] + 8

        elif len(str(i)) == 4:
            thousands = int(str(i)[0])
            hundreds_tens_units = int(str(i)[-3:])
            total += counting[thousands] + 8 + counting[hundred_tens_units]
            counting[i] = counting[thousands] + 8 + counting[hundred_tens_units]
    return total


setup1 = 'from __main__ import number_letter_counts'

print(f'Execution time: ' +
f'{(timeit.timeit("print(number_letter_counts())", setup= setup1, number=1))}.')
