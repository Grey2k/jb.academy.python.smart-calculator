# the list "walks" is already defined
# your code here
total = 0
for day in walks:
    total += day.get('distance', 0)

print(total // len(walks))
