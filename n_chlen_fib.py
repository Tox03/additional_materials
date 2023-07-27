import sys
import decimal

#sys.setrecursionlimit(5000)  # увеличивает лимит для интерактивного решения (без этого можно вычислить только 500), не работает

def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


def formulaFib(n):
    root_5 = 5 ** 0.5
    phi = (1 + root_5) / 2

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


def formulaFibWithDecimal(n):
    decimal.getcontext().prec = 10000  # Увеличенный лимит для данной формулы (без этого 1475)

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)

print(iterativeFib(1000000))