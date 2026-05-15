def digit_to_char(d):
    return "0123456789ABCDEF"[d]

def ten_to_n(x, n):
    if x < n:
        return digit_to_char(x)
    return ten_to_n(x // n, n) + digit_to_char(x % n)