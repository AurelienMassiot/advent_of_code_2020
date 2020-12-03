def read_array(filename):
    with open(filename) as file:
        array2d = [[character for character in line.split()] for line in file]
    return array2d


def move(wide, x, y, move_down, move_right):
    if y + move_right < wide:
        return x + move_down, y + move_right
    else:
        return x + move_down, y + move_right - wide


def is_tree(location):
    return True if location == '#' else False


def traverse_map(map, move_down, move_right):
    x, y = 0, 0
    wide = len(map[0][0])
    n_trees = 0
    for height in range(len(map) - 1):
        x, y = move(wide, x, y, move_down, move_right)
        try:
            if is_tree(map[x][0][y]):
                n_trees += 1
        except:
            pass
    return n_trees


def first_star():
    map = read_array('input.txt')
    n_trees = traverse_map(map, 1, 3)
    return n_trees


def second_star():
    map = read_array('input.txt')
    trees_multiplied = traverse_map(map, 1, 1)
    trees_multiplied *= traverse_map(map, 1, 3)
    trees_multiplied *= traverse_map(map, 1, 5)
    trees_multiplied *= traverse_map(map, 1, 7)
    trees_multiplied *= traverse_map(map, 2, 1)
    return trees_multiplied


if __name__ == "__main__":
    print(first_star())
    print(second_star())
