from math import floor, sqrt


def is_divisor(num, i):
    if num % i == 0:
        return True
    else:
        return False


def triangle_divisors(num):

    divisors_count = 0
    number_a = 0
    number_b = 0
    while divisors_count <= num:
        divisors_count = 0
        number_a += 1
        number_b += number_a
        for i in range(1, floor(sqrt(number_b)) + 1):
            if is_divisor(number_b, i):
                divisors_count += 2
                print(divisors_count)
    return number_b


print(triangle_divisors(500))
