# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
kids_groups = dict.fromkeys(groups)

n = int(input().strip())

started = {}
for i in range(n):
    started[groups[i]] = int(input().strip())

kids_groups.update(started)

print(kids_groups)
