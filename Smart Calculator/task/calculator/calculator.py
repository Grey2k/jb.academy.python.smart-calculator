from string import ascii_letters

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
    def __init__(self):
        self.variables = {}
        self.operands = []

    def start(self, operands: list):
        try:
            self.operands = self.__convert(operands)

            # print(self.operands)
        except Exception:
            raise ValueError('Invalid expression')

    def calculate(self):
        stack = []

        if not self.operands:
            raise ValueError('Invalid expression')

        if '=' in self.operands:
            if len(self.operands) != 3:
                raise ValueError('Invalid assignment')

            value = self.operands[1]

            if isinstance(value, int):
                self.variables[self.operands[0]] = self.operands[1]
            else:
                value = self.variables.get(self.operands[1])

                if value is None:
                    raise ValueError('Unknown variable')
                self.variables[self.operands[0]] = value
            return None

        for operand in self.operands:
            if isinstance(operand, int):
                stack.append(operand)
                continue

            if operand in OPERATIONS:
                second = stack.pop()
                first = stack.pop()

                if operand == OPERATOR_PLUS:
                    stack.append(first + second)
                    continue

                if operand == OPERATOR_MINUS:
                    stack.append(first - second)
                    continue

                if operand == OPERATOR_MULTIPLY:
                    stack.append(first * second)
                    continue

                if operand == OPERATOR_DIVIDE:
                    stack.append(first / second)
                    continue

                if operand == OPERATOR_POW:
                    stack.append(first ** second)
                    continue

            val = self.variables.get(operand)

            if val is None:
                raise ValueError('Unknown Variable')
            stack.append(val)

        return int(stack[-1])

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
                found = False
                while stack:
                    val = stack.pop()
                    if val == '(':
                        found = True
                        break

                    result.append(val)

                if not found:
                    raise ValueError('Invalid expression')

                continue

        while stack:
            val = stack.pop()
            if val == '(':
                raise ValueError('Invalid expression')

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
                raise ValueError('Invalid identifier')

        if digit and char.isdigit():
            item += char
            continue

        if operator and char in OPERATIONS:
            if char == item:
                if char in {OPERATOR_PLUS, OPERATOR_MINUS}:
                    continue
                else:
                    raise ValueError('Invalid expression')
            if char != item:
                raise ValueError('Invalid expression')

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
                raise ValueError('Invalid identifier')

    if item.strip().lstrip('-+').isdigit():
        items.append(int(item.strip().lstrip('+')))
    elif item:
        items.append(item)

    return items


calculator = Calculator()

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

        # print(operands_seq)

        calculator.start(operands_seq)
        calc_result = calculator.calculate()

        if calc_result is None:
            continue
    except ValueError as err:
        print(err)
        continue

    print(calc_result)

print('Bye!')
