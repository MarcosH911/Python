import decimal

decimales = int(input("Decimales: ")) + 1

decimal.getcontext().prec = decimales

numero = 10 ** (decimales - 1)

euler = (decimal.Decimal(1) + decimal.Decimal(1) / decimal.Decimal(numero)) ** decimal.Decimal(numero)
print(euler)
