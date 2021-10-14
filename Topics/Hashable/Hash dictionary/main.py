from collections.abc import Hashable

# create your dictionary here
objects_dict = {}

for item in objects:
    if not isinstance(item, Hashable):
        continue

    objects_dict[item] = hash(item)
