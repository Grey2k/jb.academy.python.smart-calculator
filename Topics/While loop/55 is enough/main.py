# put your code here
STOP = 55
numbers = []

while True:
    number = int(input().strip())
    if number == STOP:
        break

    numbers.append(number)

print(len(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers)))
