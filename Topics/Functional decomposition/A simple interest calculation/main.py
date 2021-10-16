def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time) / 100
    return interest, amount + interest


def print_result(interest, total_amount):
    print('The interest is: {}'.format(interest))
    print('The total amount is: {}'.format(total_amount))
