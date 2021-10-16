phrase = input().strip()

start = phrase.find('old')
end = phrase.rfind('old')

print(start if start > end else end)
