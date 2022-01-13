def iterative_binary_search(array, element):
    left = 0
    right = len(array)

    if array[0] > element or element > array[-1]:
        return -1

    while right >= left:
        mid = (left + right) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            right = mid - 1
        elif array[mid] < element:
            left = mid + 1
    return -1


def recursive_binary_search(array, element):

    if len(array) == 0:
        return False

    else:
        mid = len(array) // 2
        if array[mid] == element:
            return True
        elif array[mid] > element:
            return recursive_binary_search(array[:mid], element)
        elif array[mid] < element:
            return recursive_binary_search(array[mid:], element)
