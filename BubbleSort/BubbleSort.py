import random


def bubble_sort(array_to_be_sorted):
    for pass_number in range(len(array_to_be_sorted) - 1, 0, -1):
        for i in range(pass_number):
            if array_to_be_sorted[i] > array_to_be_sorted[i + 1]:
                temp = array_to_be_sorted[i]
                array_to_be_sorted[i] = array_to_be_sorted[i + 1]
                array_to_be_sorted[i + 1] = temp
            print(array_to_be_sorted)
        print("-------------------------------------------------")


# array = ["E", "X", "A", "M", "P", "L", "E"]
array = []
for x in range(10):
    array.append(random.randint(0, 1000))
print('Initial Array: ')
print(array)
bubble_sort(array)
