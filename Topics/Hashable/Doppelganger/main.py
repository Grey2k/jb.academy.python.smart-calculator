from collections.abc import Hashable

# the object_list has already been defined
# write your code here
hash_map = {}

for i in object_list:
    if not isinstance(i, Hashable):
        continue

    if i not in hash_map:
        hash_map[i] = 1
        continue

    hash_map[i] += 1

counter = 0
for val in hash_map.values():
    if val > 1:
        counter += val

print(counter)
