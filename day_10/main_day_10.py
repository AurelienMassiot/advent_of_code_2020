from collections import Counter
from functools import lru_cache


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def substract_previous(n_list):
    return [y - x for x, y in zip(n_list, n_list[1:])]


def compute_combinations(n_list, i):
    @lru_cache(None)
    def compute_combinations_dp(i):
        if i == len(n_list) - 1:
            return 1
        n_combinations = 0
        for j in range(i + 1, len(n_list)):
            if n_list[j] - n_list[i] <= 3:
                n_combinations += compute_combinations_dp(j)
        return n_combinations

    n_combinations = compute_combinations_dp(i)
    return n_combinations


def first_star():
    n_list = read_text_file_lines('input.txt')
    n_list.append(0)
    n_list.append(max(n_list) + 3)
    n_list.sort()
    jolts_differences = substract_previous(n_list)
    counts = Counter(jolts_differences)
    return counts[1] * counts[3]


def second_star():
    n_list = read_text_file_lines('input.txt')
    n_list.append(0)
    n_list.append(max(n_list) + 3)
    n_list.sort()
    n_combinations = compute_combinations(n_list, 0)
    return n_combinations


if __name__ == "__main__":
    print(first_star())
    print(second_star())
