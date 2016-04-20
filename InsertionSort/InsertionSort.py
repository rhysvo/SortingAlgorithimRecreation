import random


def insertion_sort(array_to_be_sorted):
    for i in range(1, len(array_to_be_sorted)):
        temp = array_to_be_sorted[i]
        j = i
        while j > 0 and temp < array_to_be_sorted[j - 1]:
            array_to_be_sorted[j] = array_to_be_sorted[j - 1]
            j -= 1
        array_to_be_sorted[j] = temp
        print(array_to_be_sorted)
        print("--------------------------------------------------")


array = []
for x in range(10):
    array.append(random.randint(100, 1000))
print("Initial array: ")
print(array)
print("==================================================")
insertion_sort(array)
