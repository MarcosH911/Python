import decimal

factorial = 1
numero = 1
euler = 0

decimales = int(input("Decimales: "))

decimal.getcontext().prec = decimales + 1

if decimales > 100:
    bucle = decimales + 10
else:
    bucle = decimales + 5

for i in range(bucle):
    for x in range(numero, 0, -1):
        factorial = factorial * x
    euler = decimal.Decimal(1) / decimal.Decimal(factorial) + decimal.Decimal(euler)
    numero = numero + 1
    factorial = 1

print(decimal.Decimal(1) / decimal.Decimal(factorial) + decimal.Decimal(euler))
