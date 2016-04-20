import random


def selection_sort(array_to_be_sorted):
    for i in range(len(array_to_be_sorted)):
        smallest_value = i
        for k in range(i + 1, len(array_to_be_sorted)):
            if array_to_be_sorted[k] < array_to_be_sorted[smallest_value]:
                smallest_value = k

        swap(array_to_be_sorted, smallest_value, i)
        print(array_to_be_sorted)
        print("-------------------------------------------------")


def swap(array_to_swap, value1, value2):
    temp = array_to_swap[value1]
    array_to_swap[value1] = array_to_swap[value2]
    array_to_swap[value2] = temp


array = []
for x in range(10):
    array.append(random.randint(100, 1000))
print(array)
print("Sorting array: ")
selection_sort(array)
