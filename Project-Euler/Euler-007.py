prime_list = [2, 3]
num = 3

while len(prime_list) < 10001:
    for prime in prime_list:
        if num % prime == 0:
            num += 2
            break
    else:
        prime_list.append(num)
        num += 2
print(prime_list[-1])
