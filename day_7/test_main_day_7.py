from day_7.main_day_7 import *

#FIXME Tests are currently dependent, because of side effects from the visited dictionary

def test_count_bags_containing_one_container():
    # Given
    this_graph_key_is_contained_in_values = {'shiny gold': [(1, 'light red')]}

    # When

    DFS_simple(this_graph_key_is_contained_in_values, 'shiny gold')

    # Then
    assert len(visited_dfs_simple) - 1 == 1


def test_count_bags_containing_one_two_containers():
    # Given
    this_graph_key_is_contained_in_values = {'shiny gold': [(1, 'bright white'), (2, 'muted yellow')]}

    # When
    DFS_simple(this_graph_key_is_contained_in_values, 'shiny gold')

    # Then
    assert len(visited_dfs_simple) - 1 == 2


def test_count_bags_containing_one_simple_tree_one_container():
    # Given
    this_graph_key_is_contained_in_values = {'bright white': [(1, 'light red')],
                                             'shiny gold': [(1, 'bright white')]}

    # When

    DFS_simple(this_graph_key_is_contained_in_values, 'shiny gold')

    # Then
    assert len(visited_dfs_simple) - 1 == 2


def test_count_bags_containing_one_simple_tree_two_containers():
    # Given
    this_graph_key_is_contained_in_values = {'bright white': [(1, 'light red'), (3, 'dark orange')],
                                             'shiny gold': [(1, 'bright white'), (2, 'muted yellow')]}

    # When

    DFS_simple(this_graph_key_is_contained_in_values, 'shiny gold')

    # Then
    assert len(visited_dfs_simple) - 1 == 4


def test_count_bags_containing_one_complex():
    # Given
    this_graph_key_is_contained_in_values = {'bright white': [(1, 'light red'), (3, 'dark orange')],
                                             'muted yellow': [(2, 'light red'), (4, 'dark orange')],
                                             'shiny gold': [(1, 'bright white'), (2, 'muted yellow')]}

    # When
    DFS_simple(this_graph_key_is_contained_in_values, 'shiny gold')

    # Then
    assert len(visited_dfs_simple) - 1 == 4


def test_first_star_test():
    # Given
    lines = read_text_file_lines('test_input.txt')

    # When
    graph_key_is_contained_in_values, graph_key_contains_values = build_graphs(lines)
    DFS_simple(graph_key_is_contained_in_values, 'shiny gold')

    # Then
    assert len(visited_dfs_simple) - 1 == 4
