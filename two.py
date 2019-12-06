from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=2)

input_data = [int(i) for i in puzzle.input_data.split(',')]

def partone(input_list):
    from itertools import zip_longest
    def grouper(iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)
    input_data[1] = 12
    input_data[2] = 2
    for i in grouper(input_data, 4):
        if i[0] == 1:
            input_data[i[3]] = input_data[i[1]] + input_data[i[2]]
        elif i[0] == 2:
            input_data[i[3]] = input_data[i[1]] * input_data[i[2]]
        elif i[0] == 99:
            return input_data[0]

def parttwo(input_list, noun, verb):
    from itertools import zip_longest
    def grouper(iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)
    input_list[1] = noun
    input_list[2] = verb
    for i in grouper(input_list, 4):
        if i[0] == 1:
            input_list[i[3]] = input_list[i[1]] + input_list[i[2]]
        elif i[0] == 2:
            input_list[i[3]] = input_list[i[1]] * input_list[i[2]]
        elif i[0] == 99:
            return input_list[0], noun, verb

from itertools import product
from copy import deepcopy
for i, j in product([i for i in range(0, 100)], repeat=2):
    list_copy = deepcopy(input_data)
    output, noun, verb = parttwo(input_list=list_copy, noun=i, verb=j)
    if output == 19690720:
        print("result: {}".format(100 * noun + verb))
        break
