def bubble_sort(array):
    for x in range(len(array) - 1, 0, -1):
        for y in range(x):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
    return array
