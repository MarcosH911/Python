num = 2520
x = 1
while True:
    if num % x == 0:
        if x == 20:
            break
        x += 1
    else:
        x = 1

        num += 2520
print(num)
