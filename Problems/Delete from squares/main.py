key = int(input())

if key not in squares:
    print('There is no such key')
else:
    print(squares.get(key))
    del squares[key]

print(squares)
