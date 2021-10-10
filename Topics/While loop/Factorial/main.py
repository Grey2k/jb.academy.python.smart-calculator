n = int(input().strip())

factorial = 1

if n <= 0:
    factorial = 0

while n > 0:
    factorial *= n
    n -= 1

print(factorial)
