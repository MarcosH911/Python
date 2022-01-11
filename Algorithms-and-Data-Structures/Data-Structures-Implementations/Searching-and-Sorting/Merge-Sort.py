def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        left_index = 0
        right_index = 0
        index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                array[index] = left_half[left_index]
                left_index += 1
            else:
                array[index] = right_half[right_index]
                right_index += 1
            index += 1

        while left_index < len(left_half):
            array[index] = left_half[left_index]
            left_index += 1
            index += 1

        while right_index < len(right_half):
            array[index] = right_half[right_index]
            right_index += 1
            index += 1

    return array
