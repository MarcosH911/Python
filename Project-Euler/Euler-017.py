# Unfinished
from math import floor


def number_letter_count(num):
    letter_sum = 0
    number_values = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7,
                     16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 13,
                     200: 13, 300: 15, 400: 14, 500: 14, 600: 13, 700: 15, 800: 15, 900: 14, 1000: 11}

    for i in range(1, num + 1):
        number = i

        if number < 20 or number == 1000:
            letter_sum += number_values[number]

        elif number < 100:
            first_digit = int(str(number)[-1])
            second_digit = floor(number / 10) * 10
            letter_sum += number_values[second_digit]

            try:
                letter_sum += number_values[first_digit]
            except KeyError:
                pass

        else:
            first_digit = int(str(number)[-1])
            second_digit = int(str(number)[-2]) * 10
            third_digit = floor(number / 100) * 100
            last_two_digits = first_digit + second_digit

            if 20 > last_two_digits > 10:
                letter_sum += number_values[third_digit] + number_values[last_two_digits]

            else:
                letter_sum += number_values[third_digit]

                try:
                    letter_sum += number_values[second_digit]
                except KeyError:
                    pass
                try:
                    letter_sum += number_values[first_digit]
                except KeyError:
                    pass

    return letter_sum


print(number_letter_count(1000))
