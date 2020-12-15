def play_alcohol_game_elves(starting_numbers, turns):
    memory = {}
    for i, number in enumerate(starting_numbers):
        memory[number] = i + 1
    spoken_number = 0
    for turn_number in range(len(starting_numbers) + 1, turns):
        previous_time = memory.get(spoken_number, None)
        memory[spoken_number] = turn_number
        if previous_time is None:
            spoken_number = 0
        else:
            spoken_number = turn_number - previous_time
    return spoken_number


def first_star():
    return play_alcohol_game_elves(starting_numbers=[0, 1, 4, 13, 15, 12, 16], turns=2020)


def second_star():
    return play_alcohol_game_elves(starting_numbers=[0, 1, 4, 13, 15, 12, 16], turns=30000000)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
