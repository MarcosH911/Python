sum_of_squares = 0
square_of_sum = 0
num = 0

for x in range(101):
    sum_of_squares += x ** 2

for i in range(101):
    num += i

square_of_sum = num ** 2

difference = square_of_sum - sum_of_squares
print(difference)
