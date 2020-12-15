def read_input(path):
    with open(path, 'r') as input_file:
        lines = input_file.read().split('\n')
    return lines


def parse_lines(lines):
    first_departure = int(lines[0])
    buses = [(int(bus), offset)
             for offset, bus in enumerate(lines[1].split(','))
             if bus != 'x']
    return first_departure, buses


def first_bus(earliest_departure, buses_with_offsets):
    departure = earliest_departure
    while True:
        for bus, _ in buses_with_offsets:
            if departure % bus == 0:
                wait_time = departure - earliest_departure
                return bus * wait_time
        departure += 1


# taken from: https://dev.to/qviper/advent-of-code-2020-python-solution-day-13-24k4
# this theorem may help https://en.wikipedia.org/wiki/Chinese_remainder_theorem
def timestamp_sync(bus_with_offsets):
    mods = {bus: -i % bus for bus, i in bus_with_offsets}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val


def first_star():
    first_departure, busses_with_offsets = parse_lines(read_input('input.txt'))
    res = first_bus(first_departure, busses_with_offsets)
    return res


def second_star():
    _, busses_with_offsets = parse_lines(read_input('input.txt'))
    timestamp = timestamp_sync(busses_with_offsets)
    return timestamp


if __name__ == "__main__":
    print(first_star())
    print(second_star())
