def shell_sort(array):
    sublist_count = len(array) // 3

    while sublist_count > 0:
        for start in range(sublist_count):
            gap_insertion_sort(array, start, sublist_count)
        sublist_count //= 2
    return array


def gap_insertion_sort(array, start, gap):

    for i in range(start + gap, len(array), gap):
        current_value = array[i]
        position = i

        while position >= gap and array[position - gap] > current_value:
            array[position] = array[position - gap]
            position -= gap
        array[position] = current_value
