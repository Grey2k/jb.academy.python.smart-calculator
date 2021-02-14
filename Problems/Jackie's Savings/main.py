def final_deposit_amount(*interests, amount=1000):
    for interest in interests:
        amount = amount * round((100 + interest) / 100, 2)

    return round(amount, 2)
