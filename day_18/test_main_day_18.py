from main_day_18 import *


def test_evaluate_expression_1():
    # Given
    expression_1 = '1 + 2'
    expression_2 = '1 + 2 * 3'
    expression_3 = '1 + 2 * 3 + 4 * 5 + 6'
    expression_4 = '1 + (2 * 3)'
    expression_5 = '1 + (2 * 3) + (4 * (5 + 6))'
    expression_6 = '2 * 3 + (4 * 5)'
    expression_7 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    expression_8 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    expression_9 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

    # When # Then
    assert evaluate_expression_1(expression_1) == 3
    assert evaluate_expression_1(expression_2) == 9
    assert evaluate_expression_1(expression_3) == 71
    assert evaluate_expression_1(expression_4) == 7
    assert evaluate_expression_1(expression_5) == 51
    assert evaluate_expression_1(expression_6) == 26
    assert evaluate_expression_1(expression_7) == 437
    assert evaluate_expression_1(expression_8) == 12240
    assert evaluate_expression_1(expression_9) == 13632


def test_evaluate_expression_2():
    # Given
    expression_1 = '1 + 2'
    expression_2 = '1 + 2 * 3'
    expression_3 = '1 + 2 * 3 + 4 * 5 + 6'
    expression_4 = '1 + (2 * 3)'
    expression_5 = '1 + (2 * 3) + (4 * (5 + 6))'
    expression_6 = '2 * 3 + (4 * 5)'
    expression_7 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    expression_8 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    expression_9 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

    # When # Then
    assert evaluate_expression_2(expression_1, evaluator_2) == 3
    assert evaluate_expression_2(expression_2, evaluator_2) == 9
    assert evaluate_expression_2(expression_3, evaluator_2) == 231
    assert evaluate_expression_2(expression_4, evaluator_2) == 7
    assert evaluate_expression_2(expression_5, evaluator_2) == 51
    assert evaluate_expression_2(expression_6, evaluator_2) == 46
    assert evaluate_expression_2(expression_7, evaluator_2) == 1445
    assert evaluate_expression_2(expression_8, evaluator_2) == 669060
    assert evaluate_expression_2(expression_9, evaluator_2) == 23340
