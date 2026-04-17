def make_payment(P):
    """
    Checking the correctness of the payment
    """
    try:
        P = float(P)

        if 20 <= P <= 1000:
            print('Успех')
        else:
            print('Повторить попытку')

    except(TypeError, ValueError):
        print('Не удалось преобразовать в число')

make_payment(2000)