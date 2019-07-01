"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import timeit
import os


def process_file(path):
    with open(path, 'r') as f:
        reader = f.read()
        names_list = reader.split('","')
        names_list[0] = names_list[0][1:]
        names_list[-1] = names_list[-1][:-1]

        return sorted(names_list)


def get_alphabet(names_list):
    counter = 1
    alpha = {}
    for name in names_list:
        if name[0] not in alpha:
            alpha[name[0]] = counter
            counter += 1
    return alpha


def name_scores(file_path):
    names_list = process_file(file_path)
    alphabet = get_alphabet(names_list)
    total_score = 0

    for name in names_list:
        name_score = 0
        index_score = names_list.index(name) + 1
        for letter in name:
            name_score += alphabet[letter]
        name_score = name_score * index_score
        total_score += name_score

    return total_score


file_path = os.path.join('files', 'problem_22.txt')

print(f'Execution time: ' +
      f'{timeit.timeit("print(name_scores(file_path))", setup="from __main__ import name_scores, file_path",  number=1)}.')
