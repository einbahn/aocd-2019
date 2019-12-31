from math import prod
from aocd.models import Puzzle

def parse_opcode(opcode):
    temp_opcode = str(opcode).zfill(5)
    return (int(temp_opcode[2]), int(temp_opcode[1]), int(temp_opcode[0])), int(temp_opcode[3:])


def make_argv(data, index, argc, modes, relative_base):
    values = []
    indexes = [i for i in range(index+1, index+argc)]
    for mode, id in zip(modes, indexes):
        if mode == 0:
            values.append(data[id])
        elif mode == 1:
            values.append(id)
        elif mode == 2:
            values.append(data[id] + relative_base)
    return values

    
def lookup_argc(lookup_dict, opcode):
    return lookup_dict[opcode]

def IntcodeComputer(data):
    index = 0
    relative_base = 0
    while True:
        modes, opcode = parse_opcode(data[index])
        argc = lookup_argc(argc_lookup, opcode)
        argv = make_argv(data, index, argc, modes, relative_base)
        if opcode == 99:
            break
        elif opcode == 4:
            print("{}".format(data[argv[0]], end=" "))
        elif opcode == 3:
            data[argv[0]] = int(input("Enter a number: "))
        elif opcode == 1:
            data[argv[2]] = data[argv[0]] + data[argv[1]]
        elif opcode == 2:
            data[argv[2]] = data[argv[0]] * data[argv[1]]
        elif opcode == 5:
            if data[argv[0]] != 0:
                index = data[argv[1]]
                continue
        elif opcode == 6:
            if data[argv[0]] == 0:
                index = data[argv[1]]
                continue        
        elif opcode == 7:
            if data[argv[0]] < data[argv[1]]:
                data[argv[2]] = 1
            else:
                data[argv[2]] = 0
        elif opcode == 8:
            if data[argv[0]] == data[argv[1]]:
                data[argv[2]] = 1
            else:
                data[argv[2]] = 0
        elif opcode == 9:
            relative_base += data[argv[0]]
        index += argc
        continue

if __name__ == "__main__":
    puzzle = Puzzle(year=2019, day=9)
    data = [int(i) for i in puzzle.input_data.split(",")]
    padding = [0] * 10000
    data += padding
    argc_lookup = {}
    argc_lookup[99] = 2
    argc_lookup[4] = 2
    argc_lookup[3] = 2
    argc_lookup[1] = 4
    argc_lookup[2] = 4
    argc_lookup[5] = 3
    argc_lookup[6] = 3
    argc_lookup[7] = 4
    argc_lookup[8] = 4
    argc_lookup[9] = 2
    IntcodeComputer(data)