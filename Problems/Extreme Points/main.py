# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
print('min: {}'.format(min(test_dict.items(), key=lambda x: x[1])[0]))
print('max: {}'.format(max(test_dict.items(), key=lambda x: x[1])[0]))
