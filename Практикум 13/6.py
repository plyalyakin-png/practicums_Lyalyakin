for xod in range(100, 334):
    mat = 3 * xod
    digits = str(xod) + str(mat)
    if len(set(digits)) == 6:
        print(f"{xod}+{xod}+{xod}={mat}")