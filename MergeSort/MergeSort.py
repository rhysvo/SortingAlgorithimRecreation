import random


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        x = 0
        y = 0
        z = 0
        while x < len(left_half) and y < len(right_half):
            if left_half[x] < right_half[y]:
                a_list[z] = left_half[x]
                x += 1
            else:
                a_list[z] = right_half[y]
                y += 1
            z += 1

        while x < len(left_half):
            a_list[z] = left_half[x]
            x += 1
            z += 1

        while y < len(right_half):
            a_list[z] = right_half[y]
            y += 1
            z += 1


array = []
for a in range(100000):
    array.append(random.randint(100, 1000))

print("Initial Array: ")
print(array)
print("==================================================")
merge_sort(array)
print("Sorted Array: ")
print(array)
