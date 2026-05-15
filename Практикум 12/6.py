def degree5(n):
    if n == 1:
        return 0
    if n < 1 or n % 5 != 0:
        return -1

    if degree5(n // 5) == -1:
        return -1
    return degree5(n // 5) + 1
print(degree5(25))