def odd_list(a, n):
    if not a:
        return []
    if a[0] % 2 == 0:
        return [a[0]] + odd_list(a[1:], n - 1)
    return odd_list(a[1:], n - 1)