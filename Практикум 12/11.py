def ind_maxlist(a):
    if len(a) == 1:
        return 0
    idx = ind_maxlist(a[1:])
    idx += 1
    if a[0] > a[idx]:
        return 0
    return idx