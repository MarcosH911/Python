from math import floor


def largest_collatz_sequence(max_number):

    largest_count = 0
    best_number = 0

    for i in range(floor(max_number/2), max_number+1):

        number = i
        count = 0

        while number != 1:

            if number % 2 == 0:
                number /= 2
                count += 1

            else:
                number = number * 3 + 1
                count += 1

        if count > largest_count:
            best_number = i
            largest_count = count

    return best_number


print(largest_collatz_sequence(1000000))
