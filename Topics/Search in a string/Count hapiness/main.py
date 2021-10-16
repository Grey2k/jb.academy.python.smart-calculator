words = input().strip().split()

print(len(list(filter(lambda x: x == 'happy', words))))
