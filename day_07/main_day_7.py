def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


visited_dfs = {}


def DFS(graph, node):
    sum_bags = 1
    if node not in graph:
        graph[node] = []
    for n_of_this_bag, bag_type in graph[node]:
        sum_bags += n_of_this_bag * DFS(graph, bag_type)
    visited_dfs[node] = 'visited'  # for debug
    return sum_bags


visited_dfs_simple = {}


def DFS_simple(graph, node):
    if node not in graph:
        graph[node] = []
    for n_of_this_bag, bag_type in graph[node]:
        DFS_simple(graph, bag_type)
    visited_dfs_simple[node] = 'visited'


def process_contained_tokens(graph_key_is_contained_in_values, graph_key_contains_values, container, contained_tokens):
    for token in contained_tokens:
        token = token.strip()
        if token == 'no other bags':
            continue
        n_of_bag_type, bag_type = extract_number_and_bag_type(token)
        add_container_values(graph_key_contains_values, container, n_of_bag_type, bag_type)
        add_contained_values(graph_key_is_contained_in_values, bag_type, n_of_bag_type, container)


def extract_number_and_bag_type(token):
    n_of_bag_type, bag_type = token.split(' ', 1)
    bag_type = bag_type.replace('bags', '').replace('bag', '').strip()
    return int(n_of_bag_type), bag_type


def add_contained_values(graph, bag_type, n_of_bag_type, container):
    if bag_type not in graph:
        graph[bag_type] = []
    graph[bag_type].append((n_of_bag_type, container))


def add_container_values(graph, container, n_of_bag_type, bag_type):
    if container not in graph:
        graph[container] = []
    graph[container].append((n_of_bag_type, bag_type))


def build_graphs(lines):
    graph_key_is_contained_in_values = {}
    graph_key_contains_values = {}
    for line in lines:
        line = line.replace('.', '')
        container, contained = line.split(' bags contain ')
        contained_tokens = contained.split(',')
        process_contained_tokens(graph_key_is_contained_in_values, graph_key_contains_values, container,
                                 contained_tokens)
    return graph_key_is_contained_in_values, graph_key_contains_values


if __name__ == "__main__":
    lines = read_text_file_lines('input.txt')
    graph_key_is_contained_in_values, graph_key_contains_values = build_graphs(lines)

    DFS_simple(graph_key_is_contained_in_values, 'shiny gold')
    print(len(visited_dfs_simple) - 1)

    print(DFS(graph_key_contains_values, 'shiny gold') - 1)
