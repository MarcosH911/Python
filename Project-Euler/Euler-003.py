from math import sqrt


def is_prime(num):
    top_try = int(sqrt(num)) + 1
    for i in range(2, top_try, 1):
        if num % i == 0:
            return False
    return True


def largest_prime_factor(num):
    for i in range(int(sqrt(num)), 1, -1):
        if num % i == 0:
            if is_prime(i):
                return i


print(largest_prime_factor(600851475143))
