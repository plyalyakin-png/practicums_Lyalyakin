def limit_check(SMS):
    """
    Checking for message length
    """
    if len(SMS) <= 160:
        return SMS

    else:
        return SMS[:160]

print(limit_check('Без обратной смс'))