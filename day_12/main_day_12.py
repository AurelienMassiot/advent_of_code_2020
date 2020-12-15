DIRECTION_MOVES = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, 1),
    'S': (0, -1),
}

ORDERED_DIRECTIONS = ['E', 'S', 'W', 'N']


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def navigate_first_star(instructions):
    pos = 0, 0
    dir = 'E'
    for instruction in instructions:
        pos, dir = move_first_star(pos, dir, instruction)
    return pos


def navigate_second_star(instructions):
    pos = 0, 0
    waypoint_pos = 10, 1
    for instruction in instructions:
        pos, waypoint_pos = move_second_star(pos, waypoint_pos, instruction)
    return pos


def move_first_star(current_pos, current_dir, instruction):
    current_x, current_y = current_pos
    direction, value = instruction
    if direction in ('E', 'W', 'N', 'S'):
        new_pos = current_x + DIRECTION_MOVES[direction][0] * value, current_y + DIRECTION_MOVES[direction][1] * value
        return new_pos, current_dir
    elif direction in ('R', 'L'):
        rotation_dir = 1 if direction == 'R' else -1
        new_dir = get_new_direction(current_dir, rotation_dir, value)
        return current_pos, new_dir
    elif direction == 'F':
        new_instruction = current_dir, value
        return move_first_star(current_pos, current_dir, new_instruction)


def move_second_star(ship_pos, waypoint_relative_pos, instruction):
    direction, value = instruction
    if direction in ('E', 'W', 'N', 'S'):
        new_waypoint_relative_pos, _ = move_first_star(waypoint_relative_pos, direction, instruction)
        return ship_pos, new_waypoint_relative_pos
    if direction in ('R', 'L'):
        new_waypoint_relative_pos = rotate_waypoint(waypoint_relative_pos, direction, value)
        return ship_pos, new_waypoint_relative_pos
    if direction == 'F':
        new_ship_pos = ship_pos[0] + value * waypoint_relative_pos[0], ship_pos[1] + value * waypoint_relative_pos[1]
        return new_ship_pos, waypoint_relative_pos


def rotate_waypoint(waypoint_pos, direction, angle):
    clockwise_quarter_turns = count_clockwise_quarter_turns(direction, angle)
    if clockwise_quarter_turns == 0:
        return waypoint_pos[0], waypoint_pos[1]
    elif clockwise_quarter_turns == 1:
        return waypoint_pos[1], -waypoint_pos[0]
    elif clockwise_quarter_turns == 2:
        return -waypoint_pos[0], -waypoint_pos[1]
    elif clockwise_quarter_turns == 3:
        return -waypoint_pos[1], waypoint_pos[0]


def count_clockwise_quarter_turns(direction, angle):
    if direction == 'R':
        return (angle // 90) % 4
    elif direction == 'L':
        return 4 - (angle // 90) % 4


def get_new_direction(current_dir, rotation_dir, value):
    return ORDERED_DIRECTIONS[(ORDERED_DIRECTIONS.index(current_dir) + rotation_dir * (value // 90)) % 4]


def manhattan_distance_from_start_pos(current_pos):
    return abs(current_pos[0]) + abs(current_pos[1])


def parse_instruction(instruction):
    return instruction[0], int(instruction[1:])


def first_star():
    instructions = read_text_file_lines('input.txt')
    instructions = [parse_instruction(i) for i in instructions]
    final_pos = navigate_first_star(instructions)
    print('final pos', final_pos)
    return manhattan_distance_from_start_pos(final_pos)


def second_star():
    instructions = read_text_file_lines('input.txt')
    instructions = [parse_instruction(i) for i in instructions]
    final_pos = navigate_second_star(instructions)
    print('final pos', final_pos)
    return manhattan_distance_from_start_pos(final_pos)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
