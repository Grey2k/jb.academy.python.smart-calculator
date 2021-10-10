shopping_list = input().split()

total_list = {}

for item in shopping_list:
    if item not in total_list:
        total_list[item] = 1
        continue

    total_list[item] += 1

for key, value in total_list.items():
    print(f"{value} {key}")
