def count(n):
    if n < 10:
        return n
    return count(n // 10) + count(n % 10)