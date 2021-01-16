COMMAND_EXIT = '/exit'
COMMAND_HELP = '/help'

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
        print('The program calculates the sum of numbers')
        continue

    print(sum(map(int, [x for x in user_input.split() if x.strip() != ""])))

print('Bye!')
