import fileinput
from copy import deepcopy


def read_list_of_list(filename):
    return [list(l.strip()) for l in list(fileinput.input(filename))]


# y->
# x |
#
def is_occupied(grid, x, y):
    if x < 0 or y < 0:
        return False
    try:
        if grid[x][y] == '#':
            return True
    except IndexError:
        return False
    return False


def is_floor(grid, x, y):
    if x < 0 or y < 0:
        return False
    try:
        if grid[x][y] == '.':
            return True
    except IndexError:
        return False
    return False


def count_adjacent_occupied(grid, x, y):
    count = 0
    if is_occupied(grid, x + 1, y):
        count += 1
    if is_occupied(grid, x + 1, y + 1):
        count += 1
    if is_occupied(grid, x, y + 1):
        count += 1
    if is_occupied(grid, x - 1, y + 1):
        count += 1
    if is_occupied(grid, x - 1, y):
        count += 1
    if is_occupied(grid, x - 1, y - 1):
        count += 1
    if is_occupied(grid, x, y - 1):
        count += 1
    if is_occupied(grid, x + 1, y - 1):
        count += 1
    return count


def count_sight_occupied(grid, x, y):
    count = 0
    for direction_x in [-1, 0, 1]:
        for direction_y in [-1, 0, 1]:
            if not (direction_x == 0 and direction_y == 0):
                new_x = x + direction_x
                new_y = y + direction_y
                while 0 <= new_x <= len(grid) and 0 <= new_y <= len(grid[0]) and is_floor(grid, new_x, new_y) and (
                        not is_occupied(grid, new_x, new_y)):
                    new_x = new_x + direction_x
                    new_y = new_y + direction_y
                if is_occupied(grid, new_x, new_y):
                    count += 1
    return count


def will_remain_seated_first_star(grid, x, y):
    return count_adjacent_occupied(grid, x, y) < 4


def will_seat_first_star(grid, x, y):
    return count_adjacent_occupied(grid, x, y) == 0


def will_remain_seated_second_star(grid, x, y):
    return count_sight_occupied(grid, x, y) < 5


def will_seat_second_star(grid, x, y):
    return count_sight_occupied(grid, x, y) == 0


def seat_all(grid):
    new_grid = [[char.replace('L', '#') for char in line] for line in grid]
    return new_grid


def unseat_first_star(grid):
    will_remain_seated_grid = []
    for x in range(0, len(grid)):
        line_booleans = []
        for y in range(0, len(grid[0])):
            line_booleans.append(will_remain_seated_first_star(grid, x, y))
        will_remain_seated_grid.append(line_booleans)
    return will_remain_seated_grid


def seat_first_star(grid):
    will_seat_grid = []
    for x in range(0, len(grid)):
        line_booleans = []
        for y in range(0, len(grid[0])):
            line_booleans.append(will_seat_first_star(grid, x, y))
        will_seat_grid.append(line_booleans)
    return will_seat_grid


def apply_unseat(grid, will_remain_seated_grid):
    new_grid = deepcopy(grid)
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if not will_remain_seated_grid[x][y] and grid[x][y] == '#':
                new_grid[x][y] = 'L'
    return new_grid


def apply_seat(grid, will_seat_grid):
    new_grid = deepcopy(grid)
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if will_seat_grid[x][y] and grid[x][y] == 'L':
                new_grid[x][y] = '#'
    return new_grid


def unseat_second_star(grid):
    will_remain_seated_grid = []
    for x in range(0, len(grid)):
        line_booleans = []
        for y in range(0, len(grid[0])):
            line_booleans.append(will_remain_seated_second_star(grid, x, y))
        will_remain_seated_grid.append(line_booleans)
    return will_remain_seated_grid


def seat_second_star(grid):
    will_seat_grid = []
    for x in range(0, len(grid)):
        line_booleans = []
        for y in range(0, len(grid[0])):
            line_booleans.append(will_seat_second_star(grid, x, y))
        will_seat_grid.append(line_booleans)
    return will_seat_grid


def play_first_star(grid):
    grid = seat_all(grid)
    # i = 0
    while True:
        # i += 1
        # print('i', i)
        new_grid = apply_unseat(grid, unseat_first_star(grid))
        new_grid = apply_seat(new_grid, seat_first_star(new_grid))
        if new_grid == grid:
            break
        else:
            grid = new_grid
    return sum(x.count('#') for x in grid)


def play_second_star(grid):
    grid = seat_all(grid)
    while True:
        new_grid = apply_unseat(grid, unseat_second_star(grid))
        new_grid = apply_seat(new_grid, seat_second_star(new_grid))
        if new_grid == grid:
            break
        else:
            grid = new_grid
    return sum(x.count('#') for x in grid)


def first_star():
    grid = read_list_of_list('input.txt')
    return play_first_star(grid)


def second_star():
    grid = read_list_of_list('input.txt')
    return play_second_star(grid)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
