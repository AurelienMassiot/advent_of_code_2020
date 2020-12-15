import itertools


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def parse_line(line):
    if line.startswith('mask'):
        return str(line.split(' = ')[-1])
    else:
        address = line[line.index('[') + 1:line.index(']')]
        value = line.split(' = ')[-1]
        return int(address), int(value)


def is_mask(instruction):
    return isinstance(instruction, str)


def pad_binary_number_str(binary_number_str, binary_mask_str):
    return '0' * (len(binary_mask_str) - len(binary_number_str)) + binary_number_str


def memory_sum_1(initialization_program):
    memory = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in initialization_program:
        instruction = parse_line(line)
        if is_mask(instruction):
            mask = instruction
        else:
            address, value = instruction
            transformed_value = apply_binary_mask_str_to_binary_number_str(value, mask)
            memory[address] = transformed_value
    return sum(memory.values())


def memory_sum_2(initialization_program):
    memory = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in initialization_program:
        instruction = parse_line(line)
        if is_mask(instruction):
            mask = instruction
        else:
            address, value = instruction
            masked_addresses = apply_binary_mask_str_to_binary_address_str(address, mask)
            for masked_address in masked_addresses:
                memory[masked_address] = value
    return sum(memory.values())


def apply_binary_mask_str_to_binary_number_str(binary_number_str, binary_mask_str):
    binary_value = bin(binary_number_str)[2:]
    padded_binary_str = pad_binary_number_str(binary_value, binary_mask_str)
    transformed_binary_number_list = [value_bit if mask_bit == 'X' else mask_bit for (value_bit, mask_bit) in
                                      zip(padded_binary_str, binary_mask_str)]
    transformed_binary_number = ''.join(transformed_binary_number_list)
    return int(transformed_binary_number, base=2)


def apply_binary_mask_str_to_binary_address_str(binary_adress_str, binary_mask_str):
    binary_address = bin(binary_adress_str)[2:]
    padded_binary_address = pad_binary_number_str(binary_address, binary_mask_str)
    floating_masked_address_list = [value_bit if mask_bit == '0' else mask_bit for (value_bit, mask_bit) in
                                    zip(padded_binary_address, binary_mask_str)]
    floating_masked_address = ''.join(floating_masked_address_list)
    all_addresses = []
    pow_2_values = floating_masked_address.count('X')
    for combination in [list(i) for i in itertools.product([0, 1], repeat=pow_2_values)]:
        masked_address = floating_masked_address
        for floating_val in combination:
            floating_pos = masked_address.index('X')
            masked_address = masked_address[:floating_pos] + str(floating_val) + masked_address[floating_pos + 1:]
        all_addresses.append(int(masked_address, base=2))
    return all_addresses


def first_star():
    program = read_text_file_lines('input.txt')
    res = memory_sum_1(program)
    return res


def second_star():
    program = read_text_file_lines('input.txt')
    res = memory_sum_2(program)
    return res


if __name__ == "__main__":
    print(first_star())
    print(second_star())
