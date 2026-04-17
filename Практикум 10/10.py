def numbers(A, B):
    """
    Finding numbers includes '13489'
    """
    result = []

    if A > B:
        A, B = B, A

    for number in range(A, B + 1):
        if all(digit in '13489' for digit in str(number)):
            result.append(number)

    return result

print(numbers(15,40))