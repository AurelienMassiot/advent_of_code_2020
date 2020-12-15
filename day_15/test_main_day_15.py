from main_day_15 import *


def test_play_alcohol_game_elves():
    # Given When Then
    #assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=4) == 0
    assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=5) == 3
    assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=6) == 3
    assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=7) == 1
    assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=8) == 0
    assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=9) == 4
    assert play_alcohol_game_elves(starting_numbers=[0, 3, 6], turns=10) == 0
9