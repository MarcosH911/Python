def factorial_digit_sum(num):
    digit_sum = 0
    for i in range(1, num + 1):
        num *= i

    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    return digit_sum


print(factorial_digit_sum(100))
