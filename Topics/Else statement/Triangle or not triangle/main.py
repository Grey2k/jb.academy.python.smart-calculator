sum_of_angles = 0

for _ in range(3):
    sum_of_angles += int(input().strip())

if sum_of_angles == 180:
    print('The triangle is valid!')
else:
    print('The triangle is not valid!')
