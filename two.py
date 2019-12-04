from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=2)

input_data = [int(i) for i in puzzle.input_data.split(',')]

def part_one(list_of_integers):
    list_of_integers[1] = 12
    list_of_integers[2] = 2
    list_iter = iter(list_of_integers)
    try:
        opcode = next(list_iter)
        if opcode == 1:
            first_position = next(list_iter)
            second_position = next(list_iter)
            target_position = next(list_iter)
            final_value = list_of_integers[first_position] + list_of_integers[second_position]
            list_of_integers[target_position] = final_value
        elif opcode == 2:
            first_position = next(list_iter)
            second_position = next(list_iter)
            target_position = next(list_iter)
            final_value = list_of_integers[first_position] * list_of_integers[second_position]
            list_of_integers[target_position] = final_value
        elif opcode == 99:
            return list_of_integers[0]
    except:
        pass
    return list_of_integers[0]


print(part_one(input_data))

