def n_digit_fibonacci_number(digit):
    n = 1
    fibonacci = 1
    a = 0

    while len(str(fibonacci)) < digit:

        b, a = a, fibonacci
        fibonacci = a + b
        n += 1
    return n


print(n_digit_fibonacci_number(1000))
