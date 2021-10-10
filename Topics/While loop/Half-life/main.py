initial = int(input().strip())
final = int(input().strip())

days = 12
periods = 0

while initial >= final:
    periods += 1
    initial /= 2

print(periods * days)
