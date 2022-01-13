def amicable_numbers_sum(num):
    divisors_list = []
    amicables_list = set()
    for x in range(1, num + 1):
        for y in range(1, x//2 + 1):
            if x % y == 0:
                divisors_list.append(y)
        sum1 = sum(divisors_list)
        divisors_list = []
        for a in range(1, sum1//2 + 1):
            if sum1 % a == 0:
                divisors_list.append(a)
        sum2 = sum(divisors_list)
        if sum2 == x and x != sum1:
            amicables_list.add(sum1)
            amicables_list.add(sum2)
        divisors_list = []
    return sum(amicables_list)


print(amicable_numbers_sum(10000))
