def real_balance(money):
    """
    Real Amount of money with bonuses.
    """
    if money == 5 or money == 10:
        return money

    elif money == 25:
        return money + 3

    elif money == 50:
        return money + 8

    elif money == 100:
        return money + 20

    return None

print(real_balance(50))