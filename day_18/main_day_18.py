from typing import Callable

from numpy import prod


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def evaluate_expression_1(expression: str) -> int:
    res = 0
    operator = '+'
    parenthesis_depth = 0
    parenthesis_start = 0
    for i, ch in enumerate(expression):
        if ch == ' ':
            continue

        elif ch == '(':
            parenthesis_depth += 1
            if parenthesis_depth == 1:
                parenthesis_start = i + 1
        elif ch == ')':
            parenthesis_depth -= 1
            if parenthesis_depth == 0:
                res_parenthesis = evaluate_expression_1(expression[parenthesis_start:i])
                if operator == '+':
                    res += res_parenthesis
                elif operator == '*':
                    res *= res_parenthesis

        elif parenthesis_depth > 0:
            continue

        elif '0' <= ch <= '9':
            number = int(ch)
            if operator == '+':
                res += number
            elif operator == '*':
                res *= number

        elif ch == '+':
            operator = '+'
        elif ch == '*':
            operator = '*'
    return res


def evaluator_2(expression):
    # could be done with math.prod in Python 3.9...
    res = [eval(sub_expression) for sub_expression in expression.split('*')]
    return prod(res)


def evaluate_expression_2(expression: str, evaluator: Callable) -> int:
    expression_to_be_evaluated = []
    current_expression = ''
    for ch in expression:
        if ch == ' ':
            continue
        elif ch.isnumeric() or ch in ['*', '+']:
            current_expression += ch
        elif ch == '(':
            expression_to_be_evaluated.append(current_expression)
            current_expression = ''
        elif ch == ')':
            val = evaluator(current_expression)
            current_expression = expression_to_be_evaluated.pop() + str(val)
    return evaluator(current_expression)


def first_star():
    lines = read_text_file_lines('input.txt')
    res = 0
    for line in lines:
        res += evaluate_expression_1(line)
    return res


def second_star():
    lines = read_text_file_lines('input.txt')
    res = 0
    for line in lines:
        res += evaluate_expression_2(line, evaluator_2)
    return res


if __name__ == "__main__":
    print(first_star())
    print(second_star())
