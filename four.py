from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=4)


def match_two(password):
    import re
    return True if re.search(r'(\d)\1', str(password)) else False


def check_increment(password):
    import math
    hundred_thousands = math.floor(password / 100000)
    ten_thousands = math.floor((password - (hundred_thousands * 100000)) / 10000)
    thousands = math.floor((password - hundred_thousands * 100000 - ten_thousands * 10000) / 1000)
    hundreds = math.floor((password - hundred_thousands * 100000 - ten_thousands * 10000 - thousands * 1000) / 100)
    tens = math.floor((password - hundred_thousands * 100000 - ten_thousands * 10000 - thousands * 1000 - hundreds * 100) / 10)
    ones = math.floor((password - hundred_thousands * 100000 - ten_thousands * 10000 - thousands * 1000 - hundreds * 100 - tens * 10))
    if hundred_thousands <= ten_thousands <= thousands <= hundreds <= tens <= ones:
        return True
    else:
        return False


def match_only_two(password):
    pass_str = str(password)
    import re
    matches = re.findall(r'(\d)\1', pass_str)
    if matches:
        for m in matches:
            new_pattern = '(?<!{0})({0}){{1,2}}(?!{0})'.format(m)
            if re.search(new_pattern, pass_str):
                return True
        return False
    return False


if __name__ == '__main__':
    total = []
    for i in range(246515, 739105):
        if match_only_two(i) and check_increment(i):
            total.append(i)
    print("Result is {}".format(len(total)))