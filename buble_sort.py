array = [2, 7, 4, 1, 5, 3]
swaps = True

while swaps:
    swaps = False

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            swaps = True

print(array)
