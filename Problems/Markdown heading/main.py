def heading(text, level=1, sym='#'):
    if level < 1:
        level = 1
    if level > 6:
        level = 6

    return f'{sym * level} {text}'
