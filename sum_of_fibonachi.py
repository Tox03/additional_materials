def fib_sum(n):  # Сумма n чисел фибоначи
    a, b, p, q, n = 1, 1, 0, 1, n + 1
    while (n > 0):
        if (n % 2 == 0):
            p, q, n = p * p + q * q, 2 * p * q + q * q, n / 2
        else:
            a, b, n = b * q + a * q + a * p, b * p + a * q, n - 1
    return b - 1


print(fib_sum(1000000))