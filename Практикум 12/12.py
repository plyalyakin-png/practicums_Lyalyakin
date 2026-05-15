def search(a, x):
    if not a:
        return 0
    if x == a[0]:
        return 1
    return search(a[1:], x)