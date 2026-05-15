def pownum(a, n):
    if n == 0:
        return 1
    return a * pownum(a, n - 1)