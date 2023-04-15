input_array = [2, 7, 4, 1, 5, 3]


def merge_sort(array):
    half = int(len(array) / 2)

    if len(array) < 2:
        return array

    left = array[:half]
    right = array[half:]
    merge_sort(left)
    merge_sort(right)

    helper_funct_merge(left, right, array)


def helper_funct_merge(left, right, array):
    len_l = len(left)
    len_r = len(right)
    i = j = k = 0

    while i < len_l and j < len_r:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len_l:
        array[k] = left[i]
        i += 1
        k += 1
    while j < len_r:
        array[k] = right[j]
        j += 1
        k += 1
