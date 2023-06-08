def mergeSort(list_to_sort_by_merge):
    if len(list_to_sort_by_merge) <= 1:
        return list_to_sort_by_merge

    mid = len(list_to_sort_by_merge) // 2
    left = list_to_sort_by_merge[:mid]
    right = list_to_sort_by_merge[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
