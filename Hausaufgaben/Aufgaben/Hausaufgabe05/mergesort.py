def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        # and not len(list_to_sort_by_merge) < 1
        # and len(list_to_sort_by_merge) != 0    beide zeilen sind unnötig
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
                list_to_sort[i] = left[l]
                l += 1
            else:
                # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
                list_to_sort[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)

x = range(len(my_list))
plt.plot(x, my_list)
plt.show()