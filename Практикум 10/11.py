def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


N = int(input())

for num in range(1, N + 1):
    if is_prime(num):
        print(num)