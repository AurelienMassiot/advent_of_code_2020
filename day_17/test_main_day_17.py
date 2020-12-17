from main_day_17 import *
from sparray import Sparray


def test_sparray():
    A = Sparray((5, 5, 5))
    A[2, 2, 2] = 1
    A[3, 3, 3] = 1
    # print(A)
    # print(A.sum())


def test_create_array_from_lines():
    lines = read_text_file_lines('test_input.txt')
    A = create_array_from_lines(lines)
    assert A.sum() == 5


def test_count_active_neighbors():
    # Given
    A = Sparray((3, 3, 3))
    A[1, 1, 1] = 1
    A[1, 1, 0] = 1

    # When Then
    assert count_active_neighbors(A, 1, 1, 1) == 1
    assert count_active_neighbors(A, 1, 1, 0) == 1
    assert count_active_neighbors(A, 0, 0, 0) == 2
    assert count_active_neighbors(A, -1, -1, -1) == 0
    assert count_active_neighbors(A, -1, 0, 0) == 0
    assert count_active_neighbors(A, 3, 0, 0) == 0
    assert count_active_neighbors(A, -2, -2, -2) == 0


def test_count_active_neighbors_example():
    # Given
    A = Sparray((3, 3, 3))  # dimensions will be 0,1,2
    A[1, 0, 1] = 1
    A[2, 1, 1] = 1
    A[0, 2, 1] = 1
    A[1, 2, 1] = 1
    A[2, 2, 1] = 1
    B = Sparray((5, 5, 5))

    # When Then
    counts = []
    for x in range(5):
        for y in range(5):
            for z in range(5):
                counts.append(count_active_neighbors(A, x, y, z))
                B[x, y, z] = count_active_neighbors(A, x, y, z)
    counts_superior_or_equal_to_2 = [count for count in counts if count == 2 or count == 3]
    # print(counts_superior_or_equal_to_2)
    assert len(counts_superior_or_equal_to_2) >= 11
    assert len(counts_superior_or_equal_to_2) == 30


def test_simulate_cycle_one_time():
    # Given
    A = Sparray((3, 3, 3))  # dimensions will be 0,1,2
    A[1, 0, 1] = 1
    A[2, 1, 1] = 1
    A[0, 2, 1] = 1
    A[1, 2, 1] = 1
    A[2, 2, 1] = 1

    # When Then
    # print('A', A)
    new_array = simulate_cycle(A)

    assert new_array.sum() == 11


def test_simulate_cycle_two_times():
    # Given
    A = Sparray((3, 3, 3))  # dimensions will be 0,1,2
    A[1, 0, 1] = 1
    A[2, 1, 1] = 1
    A[0, 2, 1] = 1
    A[1, 2, 1] = 1
    A[2, 2, 1] = 1

    # When Then
    # print('A', A)
    for i in range(2):
        A = simulate_cycle(A)

    assert A.sum() == 21


def test_simulate_cycle_six_times():
    # Given
    A = Sparray((3, 3, 3))  # dimensions will be 0,1,2
    A[1, 0, 1] = 1
    A[2, 1, 1] = 1
    A[0, 2, 1] = 1
    A[1, 2, 1] = 1
    A[2, 2, 1] = 1

    # When Then
    for i in range(6):
        A = simulate_cycle(A)

    assert A.sum() == 112


def test_first_star():
    lines = read_text_file_lines('test_input.txt')
    A = create_array_from_lines(lines)
    for i in range(6):
        A = simulate_cycle(A)
        print(A.sum())
    assert A.sum() == 112
