def progress(a1, r, n):
    if n == 1:
        return a1
    return progress(a1 + r, r, n - 1)