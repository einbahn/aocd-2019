#!/home/user/Documents/aocd-2019/venv/bin/python3

from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=3)
ip = puzzle.input_data


def parse_direction(movement):
    _direction = movement[0]
    amount = int(movement[1:])
    return _direction, amount


class Grid(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = {}
    
    def go(self, __direction):
        if __direction == 'R':
            self.x += 1
        elif __direction == 'L':
            self.x -= 1
        elif __direction == 'U':
            self.y += 1
        elif __direction == 'D':
            self.y -= 1

    def jump(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y


def part_one():
    wire1 = [i for i in ip.split('\n')[0].split(',')]
    wire2 = [i for i in ip.split('\n')[1].split(',')]
    grid = Grid()

    def manhattan(x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    for n, wire in enumerate((wire1, wire2), 1):
        grid.jump(0, 0)
        for i in wire:
            direction, steps = parse_direction(i)
            for j in range(0, steps):
                grid.go(direction)
                coord = grid.get()
                if coord not in grid.grid:
                    grid.grid[coord] = {}
                if n not in grid.grid[coord]:
                    grid.grid[coord][n] = 1
                if 1 in grid.grid[coord] and 2 in grid.grid[coord]:
                    grid.grid[coord]['manhattan'] = manhattan((0, 0), coord)

    return min([grid.grid[i]['manhattan'] for i in grid.grid.keys() if len(grid.grid[i]) == 3])


def part_two():
    grid = Grid()
    wire1 = [i for i in ip.split('\n')[0].split(',')]
    wire2 = [i for i in ip.split('\n')[1].split(',')]

    def manhattan(x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    for n, wire in enumerate((wire1, wire2), 1):
        grid.jump(0, 0)
        steps_total = 0
        for i in wire:
            direction, steps = parse_direction(i)
            for j in range(0, steps):
                steps_total += 1
                grid.go(direction)
                coord = grid.get()
                if coord not in grid.grid:
                    grid.grid[coord] = {}
                if n not in grid.grid[coord]:
                    grid.grid[coord][n] = steps_total
                elif grid.grid[coord][n] > steps_total:
                    grid.grid[coord][n] = steps_total
                if 1 in grid.grid[coord] and 2 in grid.grid[coord]:
                    grid.grid[coord]['manhattan'] = manhattan((0, 0), coord)
                    grid.grid[coord]['combined_steps'] = grid.grid[coord][1] + grid.grid[coord][2]

    return min([grid.grid[i]['combined_steps'] for i in grid.grid.keys() if len(grid.grid[i]) == 4])


if __name__ == '__main__':
    print("Result of part one is {}".format(part_one()))
    print("Result of part two is {}".format(part_two()))
