from sparray import Sparray


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def create_array_from_lines(lines) -> Sparray:
    n = len(lines)
    A = Sparray((n, n, 3)) #0, 1, 2
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            # print(char)
            if char == '#':
                # print('line and char', line, char)
                A[i, j, 1] = 1
    return A


def simulate_cycle(array: Sparray):
    new_len_x = array.shape[0] + 2
    new_len_y = array.shape[1] + 2
    new_len_z = array.shape[2] + 2
    print('shape', array.shape[0], array.shape[1], array.shape[2])
    new_array = Sparray((new_len_x, new_len_y, new_len_z))
    for x in range(0, new_len_x):
        for y in range(0, new_len_y):
            for z in range(0, new_len_z):
                n_active_neighbors = count_active_neighbors(array, x, y, z)
                # print('n_active_neighbors', n_active_neighbors)
                if ((n_active_neighbors == 2) or (n_active_neighbors == 3)) and array[x, y, z] == 1:
                    new_array[x + 1, y + 1, z + 1] = 1
                elif n_active_neighbors == 3 and array[x, y, z] == 0:
                    new_array[x + 1, y + 1, z + 1] = 1
                else:
                    # print('remains inactive')
                    pass
    return new_array


def count_active_neighbors(array: Sparray, x, y, z):
    count = 0
    for i in range(x - 1, x + 2):
        # print('i', i)
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i == x) and (j == y) and (k == z):
                    #   print('sur place')
                    continue
                if (i < 0) or (i >= array.shape[0]) or (j < 0) or (j >= array.shape[1]) or (k < 0) or (
                        k >= array.shape[2]):
                    # print('bounding limits')
                    continue
                else:
                    # print('value', value)
                    # print('ijk', i,j,k)
                    count += array[i, j, k]
    return count


def first_star():
    lines = read_text_file_lines('input.txt')
    A = create_array_from_lines(lines)
    print(A.sum())
    for i in range(6):
        A = simulate_cycle(A)
        print(A.sum())
    return A.sum()


def second_star():
    pass


if __name__ == "__main__":
    print(first_star())
    print(second_star())
