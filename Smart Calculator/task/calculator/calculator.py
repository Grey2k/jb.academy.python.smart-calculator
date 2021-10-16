from string import ascii_letters
from collections import deque

COMMAND_EXIT = '/exit'
COMMAND_HELP = '/help'

OPERATOR_PLUS = '+'
OPERATOR_MINUS = '-'
OPERATOR_EQUAL = '='
OPERATOR_POW = '^'
OPERATOR_MULTIPLY = '*'
OPERATOR_DIVIDE = '/'

PARENTHESES = {
    '(': ')',
    ')': '('
}

OPERATIONS = {OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_MULTIPLY, OPERATOR_DIVIDE, OPERATOR_EQUAL, OPERATOR_POW}


class Calculator:
    variables = {}

    def __init__(self, operands: list):
        try:
            self.operands = self.__convert(operands)
            print(self.operands)
        except Exception:
            raise ValueError('Invalid expression')

    def calculate(self):
        pass

    @staticmethod
    def __is_variable(op: str):
        return set(op).issubset(ascii_letters)

    @staticmethod
    def __is_higher(first, second):
        if first == OPERATOR_EQUAL:
            return False

        if first in {OPERATOR_PLUS, OPERATOR_MINUS} and second not in {OPERATOR_EQUAL}:
            return False

        if first in {OPERATOR_DIVIDE, OPERATOR_MULTIPLY} \
                and second in {OPERATOR_POW, OPERATOR_DIVIDE, OPERATOR_MULTIPLY}:
            return False

        if first == OPERATOR_POW and second is OPERATOR_POW:
            return False

        return True

    def __convert(self, operands: list) -> list:
        result = []
        stack = []

        for op in operands:
            if isinstance(op, int):
                result.append(op)
                continue

            if Calculator.__is_variable(op):
                result.append(op)
                continue

            if op in OPERATIONS and (not stack or stack[-1] == '('):
                stack.append(op)
                continue

            if op in OPERATIONS:
                if not self.__is_higher(op, stack[-1]):
                    while stack and not self.__is_higher(op, stack[-1]):
                        val = stack.pop()
                        if val == '(':
                            break

                        result.append(val)

                stack.append(op)

            if op == '(':
                stack.append(op)
                continue

            if op == ')':
                while stack:
                    val = stack.pop()
                    if val == '(':
                        break

                    result.append(val)
                continue

        while stack:
            val = stack.pop()
            if val == '(':
                ValueError('Invalid expression')

            result.append(val)

        return result


def parse_str(raw_string: str) -> list:
    items = []

    item = ''

    start = True
    digit = False
    operator = False
    variable = False

    for char in raw_string.strip():
        char = char.strip()
        if not char:
            continue

        if char in PARENTHESES:
            if char == '(':
                start = True
            else:
                start = False

            if item and digit:
                items.append(int(item))
                digit = False

            if item and operator:
                items.append(item)
                operator = False

            if item and variable:
                items.append(item)
                variable = False

            item = ''
            items.append(char)
            continue

        # negative digit assumption
        if char is OPERATOR_MINUS and start:
            item += char
            digit = True
            continue

        if item == OPERATOR_MINUS and digit and start:
            if char == OPERATOR_MINUS:
                continue
            elif char.isdigit():
                item += char
                start = False
                continue
            else:
                raise ValueError('Invalid expression')

        # positive digit assumption
        if char is OPERATOR_PLUS and start:
            item += char
            digit = True
            continue

        if item == OPERATOR_PLUS and digit and start:
            if char == OPERATOR_PLUS:
                continue
            elif char.isdigit():
                item += char
                start = False
                continue
            else:
                raise ValueError('Invalid expression')

        start = False

        if not digit and not variable and not operator:
            if char.isdigit():
                digit = True
                item += char
                continue

            if char in OPERATIONS:
                operator = True
                item += char
                continue

            if char in ascii_letters:
                variable = True
                item += char
                continue

        if digit and not char.isdigit():
            items.append(int(item))
            item = ''
            digit = False

            if char in OPERATIONS:
                item += char
                operator = True
                continue
            else:
                ValueError('Invalid identifier')

        if digit and char.isdigit():
            item += char
            continue

        if operator and char in OPERATIONS:
            if char == item:
                continue
            if char != item:
                ValueError('Invalid expression')

        if operator and char not in OPERATIONS:
            items.append(item)
            item = ''
            operator = False

            if char in ascii_letters:
                variable = True
                item += char
                continue

            if char.isdigit():
                digit = True
                item += char
                continue

        if variable and char in ascii_letters:
            item += char
            continue

        if variable and char not in ascii_letters:
            items.append(item)
            item = ''
            variable = False

            if char in OPERATIONS:
                item += char
                operator = True
                continue
            else:
                ValueError('Invalid identifier')

    if item.strip().lstrip('-+').isdigit():
        items.append(int(item.strip().lstrip('+')))
    elif item:
        items.append(item)

    return items


while True:
    try:
        user_input = input().strip()

        if len(user_input) == 0:
            continue
    except EOFError:
        continue

    if user_input == COMMAND_EXIT:
        break

    if user_input == COMMAND_HELP:
        print('The program calculates math sequence with + and -')
        continue

    if user_input.startswith('/'):
        print('Unknown command')
        continue

    try:
        operands_seq = parse_str(user_input)

        print(operands_seq)

        calculator = Calculator(operands_seq)
        calc_result = calculator.calculate()

        if calc_result is None:
            continue
    except ValueError as err:
        print(err)
        continue

    print(calc_result)

print('Bye!')
