from types import MappingProxyType

input_name = input()

REPLACES = MappingProxyType({
    'é': 'e',
    'ë': 'e',
    'á': 'a',
    'å': 'a',
    'œ': 'oe',
    'æ': 'ae',
})


def normalize(name: str):
    new_name = []

    for char in name:
        if char in REPLACES:
            new_name.append(REPLACES.get(char))
            continue

        new_name.append(char)

    return ''.join(new_name)


print(normalize(input_name))
