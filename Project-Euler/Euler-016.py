def power_digit_sum(number, power):
    number_power = str(number ** power)
    digit_list = list(map(int, number_power))
    digit_sum = 0
    for i in range(len(digit_list)):
        digit_sum += digit_list[i]
    return digit_sum


print(power_digit_sum(2,1000))
