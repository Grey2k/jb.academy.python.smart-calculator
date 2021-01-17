COMMAND_EXIT = '/exit'
COMMAND_HELP = '/help'

OPERATOR_PLUS = '+'
OPERATOR_MINUS = '-'


def parse_operator(op_str: str) -> str:
    minuses = []
    pluses = []

    for char in op_str:
        if char == '+':
            pluses.append(char)
            continue

        if char == '-':
            minuses.append(char)
            continue

        raise ValueError(f'current value unexpected {char}')

    if len(pluses) > 0 and len(minuses) > 0:
        raise ValueError(f'current value unexpected {pluses} {minuses}')

    if len(pluses) > 0:
        return '+'

    return '-' if len(minuses) % 2 == 1 else '+'


def parse_str(raw_string: str) -> list:
    items = []

    raw_strings = raw_string.split()

    for item in raw_strings:
        if item.strip().lstrip('-+').isnumeric():
            items.append(int(item.strip().lstrip('+')))
            continue

        if len(item.strip()) == 0:
            continue

        items.append(parse_operator(item.strip()))

    return items


def calculate(operands_list: list) -> int:
    result = None
    current = None

    for o in operands_list:
        if result is None and isinstance(o, int):
            result = o
            continue

        if isinstance(o, int) and current is not None:
            if current == OPERATOR_MINUS:
                result -= o
                continue
            if current == OPERATOR_PLUS:
                result += o
                continue

            raise ValueError(f'current value unexpected {o}')

        if o in (OPERATOR_PLUS, OPERATOR_MINUS):
            current = o
            continue

        raise ValueError(f'current value unexpected {o}')

    return result


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
        operands = parse_str(user_input)
        calc_result = calculate(operands)
    except ValueError:
        print('Invalid expression')
        continue

    print(calc_result)

print('Bye!')
