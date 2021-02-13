# put your python code here
words = input().strip().split()

stats = {}

for word in words:
    key = word.lower()
    stats[key] = 1 if stats.get(key) is None else stats.get(key) + 1

for key, value in stats.items():
    print(f'{key} {value}')
