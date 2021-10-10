deposit = float(input().strip())

years = 0

while deposit < 700_000:
    years += 1
    deposit += deposit / 100 * 7.1

print(years)
