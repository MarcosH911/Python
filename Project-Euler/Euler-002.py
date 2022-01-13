def even_fibonacci_numbers(max_num):
    even_fibonacci_list = []
    fibonacci = 1
    a = 0
    b = 0
    while fibonacci < max_num:
        b = a
        a = fibonacci
        fibonacci = a + b
        if fibonacci < max_num and fibonacci % 2 == 0:
            even_fibonacci_list.append(fibonacci)
    return sum(even_fibonacci_list)


print(even_fibonacci_numbers(4000000))
