def inverted_number(num):
    inverted_product = str(num)[::-1]
    inverted_product = int(inverted_product)
    return inverted_product


num1 = 999
num2 = 999
number = 0
product = num1 * num2

for i in range(100):
    while product != inverted_number(product):
        num2 -= 1
        product = num1 * num2
    else:
        if product > number:
            number = product
    num1 -= 1
    num2 = 999
    product = num1 * num2
print(number)
