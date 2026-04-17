def Fibonaci_function(N):
    """
    Reads the number of first numbers and returns their values.
    """
    if N <= 0:
        return 0

    fib_nums = []
    a, b = 1, 1

    for i in range(N):
        fib_nums.append(a)
        a, b = b, a + b

    print(fib_nums)
    return None
N = int(input())
Fibonaci_function(N)
