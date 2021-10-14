first = int(input().strip())
second = int(input().strip())

if first == max(first, second):
    print(first)
else:
    print(second)

if first == min(first, second):
    print(first)
else:
    print(second)
