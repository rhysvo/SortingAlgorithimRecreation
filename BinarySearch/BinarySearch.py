def binary_search(array, value_to_be_searched):
    left_bound = 0
    right_bound = len(array) - 1
    found = False
    while left_bound <= right_bound and not found:
        middle = (left_bound + right_bound) // 2
        if array[middle] == value_to_be_searched:
            return middle
        else:
            if value_to_be_searched < array[middle]:
                right_bound = middle + 1
            else:
                left_bound = middle + 1
    if not found:
        print("Error: item not in tree")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 3))
