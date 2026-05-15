def check_prime(x, d):
    if d * d > x:
        return 1
    if x % d == 0:
        return 0
    return check_prime(x, d + 1)

def function1(x):
    if x < 2:
        return 0
    return check_prime(x, 2)