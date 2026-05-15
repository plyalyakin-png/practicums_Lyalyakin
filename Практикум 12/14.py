def numbers(x):
    if x == 0:
        return None
    print(x % 10)
    return numbers(x // 10)