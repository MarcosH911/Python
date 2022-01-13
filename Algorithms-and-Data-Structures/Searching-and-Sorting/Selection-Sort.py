def selection_sort(array):
    for x in range(len(array) - 1, 0, -1):
        max_position = 0
        for y in range(1, x+1):
            if array[y] > array[max_position]:
                max_position = y
        array[x], array[max_position] = array[max_position], array[x]
    return array
