def special_pythagorean_triplet(abcsum):
    c = 1
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if a ** 2 + b ** 2 == c ** 2:
                    if a + b + c == abcsum:
                        return a * b * c
                    else:
                        c += 1
        else:
            c += 1


print(special_pythagorean_triplet(1000))
