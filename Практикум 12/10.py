def maxlist(a):
    if len(a) == 1:
        return a[0]
    if a[0] > maxlist(a[1:]):
        return a[0]
    return maxlist(a[1:])
print(maxlist(7, 10, 2, 1))