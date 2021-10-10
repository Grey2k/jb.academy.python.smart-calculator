three_months = tuple(input().split())

found = False

for season in months:
    if season == three_months:
        found = True
        break

print(found)
