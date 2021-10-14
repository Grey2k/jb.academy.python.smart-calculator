recommended = int(input().strip())
limit = int(input().strip())
current = int(input().strip())

if recommended <= current <= limit:
    print('Normal')
elif current < recommended:
    print("Deficiency")
else:
    print("Excess")
