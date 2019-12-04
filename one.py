from aocd.models import Puzzle
import math

puzzle = Puzzle(year=2019, day=1)


def part_one():
    return sum(math.floor(int(i)/3)-2 for i in puzzle.input_data.split('\n'))


print(part_one())


def part_two(amount):
    new_amount = math.floor(int(amount)/3 - 2)
    if new_amount <= 0:
        return 0
    else:
        return new_amount + part_two(new_amount)


print(sum(part_two(i) for i in puzzle.input_data.split('\n')))
