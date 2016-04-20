import random


def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(array, lower_bound, upper_bound):
    if lower_bound < upper_bound:
        split_point = partition(array, lower_bound, upper_bound)

        quick_sort_helper(array, lower_bound, split_point - 1)
        quick_sort_helper(array, split_point + 1, upper_bound)


def partition(array_to_partition, first, last):
    pivot_value = array_to_partition[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array_to_partition[left_mark] <= pivot_value:
            left_mark += 1

        while array_to_partition[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            swap(array_to_partition, left_mark, right_mark)

    swap(array_to_partition, first, right_mark)
    return right_mark


def swap(array_to_swap, value1, value2):
    temp = array_to_swap[value1]
    array_to_swap[value1] = array_to_swap[value2]
    array_to_swap[value2] = temp


arr = []
for z in range(10):
    arr.append(random.randint(100, 1000))

print("Initial Array: ")
print(arr)
print("==================================================")
quick_sort(arr)
print("==================================================")
print("Final Array: ")
print(arr)
