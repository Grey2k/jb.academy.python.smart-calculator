# Save the input in this variable
ticket = input().strip()

# Add up the digits for each half
half1 = 0
half2 = 0

for i, n in enumerate(ticket):
    if i < (len(ticket) // 2):
        half1 += int(n)
    else:
        half2 += int(n)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
