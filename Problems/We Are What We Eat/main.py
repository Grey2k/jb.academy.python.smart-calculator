# the list "meals" is already defined
# your code here
total = 0
for item in meals:
    total += item.get('kcal', 0)

print(total)
