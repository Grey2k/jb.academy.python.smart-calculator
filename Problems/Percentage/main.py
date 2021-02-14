def get_percentage(number, ndigits=None):
    if ndigits is None:
        return f'{int(round(number * 100))}%'

    return f'{round(number * 100, ndigits)}%'
