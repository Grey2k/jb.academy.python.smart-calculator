sentence = input().lower()
punctuation = ',.!?'

print(''.join([c for c in sentence if c not in punctuation]))
