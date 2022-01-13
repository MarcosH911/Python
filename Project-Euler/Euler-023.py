# Unfinished
def abundant_numbers(max_num):
    divisors_list = []
    for x in range(1, max_num):
        for y in range(1, x//2 + 1):
            if x % y == 0:
                divisors_list.append(y)
        if sum(divisors_list) > x:
            yield x
        divisors_list = []


def non_abundant_sum():
    total_sum = 0
    abundant_numbers_list = []
    for i in abundant_numbers(14075):
        abundant_numbers_list.append(i)
        
    for x in range(1, 28124):
        keep_going = True
        while keep_going:
            if x % 12 == 0 and x != 12:
                break
            elif x % 18 == 0 and x != 18:
                break
            elif x % 20 == 0 and x != 20:
                break
            elif x % 30 == 0 and x != 30:
                break
            elif x % 42 == 0 and x != 42:
                break
            elif x % 56 == 0 and x != 56:
                break
            elif x % 66 == 0 and x != 66:
                break
            elif x % 70 == 0 and x != 70:
                break

            for num1 in abundant_numbers_list:
                if num1 >= x:
                    break
                for num2 in abundant_numbers_list:
                    if num2 >= x:
                        break
                    if num1 + num2 == x:
                        keep_going = False

            if keep_going:
                total_sum += x
                keep_going = False

    return total_sum
