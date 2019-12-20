from aocd.models import Puzzle
from math import prod
puzzle = Puzzle(year=2019, day=5)

input_data = [int(i) for i in puzzle.input_data.split(',')]
input_data_copy = input_data


def partone(input_list, index=None):
    if index is None:
        index = 0
    if input_list[0] == 4 and input_list[2] == 99:
        print("The diagnostic code is {}".format(input_data_copy[input_list[1]]))
        return
    else:
        if input_list[0] == 3:
            input_data_copy[input_list[1]] = 1
            index += 2
            return partone(input_data_copy[index::], index)
        elif input_list[0] == 4:
            print("The current test has return code {}".format(input_data_copy(input_list[1])))
            index += 2
            return partone(input_data_copy[index::], index)
        elif input_list[0] == 1:
            input_data_copy[input_list[3]] = input_data_copy[input_list[1]] + input_data_copy[input_list[2]]
            index += 4
            return partone(input_data_copy[index::], index)
        elif input_list[0] == 2:
            input_data_copy[input_list[3]] = input_data_copy[input_list[1]] * input_data_copy[input_list[2]]
            index += 4
            return partone(input_data_copy[index::], index)
        elif len(str(input_list[0])) == 4:
            str_input = str(input_list[0])
            opcode = str_input[-2::]
            param_mode_1 = str_input[-3]
            param_mode_2 = str_input[-4]
            if param_mode_1 == '0':
                first_val = input_data_copy[input_list[1]]
            else:
                first_val = input_list[1]
            if param_mode_2 == '0':
                second_val = input_data_copy[input_list[2]]
            else:
                second_val = input_list[2]
            if opcode == '01':
                input_data_copy[input_list[3]] = first_val + second_val
            elif opcode == '02':
                input_data_copy[input_list[3]] = first_val * second_val
            index += 4
            return partone(input_data_copy[index::], index)

partone(input_data)


def parse_opcode(opcode):
    temp_opcode = str(opcode).zfill(4)
    return ([int(temp_opcode[1]), int(temp_opcode[0])], int(temp_opcode[2:]))

def get_val_from_modes(data, modes, argv):
    return [i[0] if i[1] == 1 else data[i[0]] for i in zip(argv, modes)]

def make_argv(data, curr_index, argc):
    return data[curr_index+1:curr_index+argc+1]

def IntcodeComputer(data):
    data = [int(i) for i in data.split(",")]
    index = 0
    while True:
        try:
            modes, opcode = parse_opcode(data[index])
            argc = argc_lookup[opcode]
            argv = make_argv(data, index, argc)
            args = get_val_from_modes(data, modes, argv)
        except:
            print("unexpectedly reached the end of the list, stopping...")
            break
        if opcode == 99:
            break
        elif opcode == 4:
            return data[argv[0]]
        elif opcode == 3:
            data[argv[0]] = int(input("Enter a number: "))
        elif opcode == 1:
            data[argv[2]] = sum(args)
        elif opcode == 2:
            data[argv[2]] = prod(args)
        elif opcode == 5:
            if args[0] != 0:
                index = args[1]
                continue
        elif opcode == 6:
            if args[0] == 0:
                index = args[1]
                continue        
        elif opcode == 7:
            if args[0] < args[1]:
                data[argv[2]] = 1
            else:
                data[argv[2]] = 0
        elif opcode == 8:
            if args[0] == args[1]:
                data[argv[2]] = 1
            else:
                data[argv[2]] = 0
        index += argc + 1
        continue

if __name__ == "__main__":    
    argc_lookup = {}
    argc_lookup[99] = 1
    argc_lookup[4] = 1
    argc_lookup[3] = 1
    argc_lookup[1] = 3
    argc_lookup[2] = 3
    argc_lookup[5] = 2
    argc_lookup[6] = 2
    argc_lookup[7] = 3
    argc_lookup[8] = 3
    #mock_data = "3,9,8,9,10,9,4,9,99,-1,8"
    #mock_data = '3,9,7,9,10,9,4,9,99,-1,8'
    #mock_data = '3,3,1108,-1,8,3,4,3,99'
    #mock_data = '3,3,1107,-1,8,3,4,3,99'
    #mock_data = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
    #mock_data = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
    #mock_data = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
    #IntcodeComputer(puzzle.input_data)
    print("The result is {}".format(IntcodeComputer(puzzle.input_data)))