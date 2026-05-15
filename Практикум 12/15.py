def ten_to_bin(x):
    if x < 2:
        return str(x)
    return ten_to_bin(x // 2) + str(x % 2)