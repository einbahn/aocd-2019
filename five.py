from aocd.models import Puzzle

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
