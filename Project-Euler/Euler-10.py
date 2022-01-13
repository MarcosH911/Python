from math import sqrt, floor


def is_prime(num):
    top_try = floor(sqrt(num)) + 1
    for i in range(2, top_try):
        if num % i == 0:
            return False
    return True


def sum_primes(max_prime):
    primes_sum = 2
    for x in range(3, max_prime, 2):
        if is_prime(x):
            primes_sum += x
            # print(x)
    return primes_sum


print(sum_primes(200))
