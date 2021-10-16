def what_to_do(instructions: str) -> str:
    if not instructions.startswith('Simon says') and not instructions.endswith('Simon says'):
        return "I won't do it!"

    command: str = 'I '

    if instructions.startswith('Simon says'):
        command += instructions[len('Simon says') + 1:]

    if instructions.endswith('Simon says'):
        command += instructions[:len('Simon says') + 1]

    return command
