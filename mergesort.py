def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2         #divide array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)       #recursively sort both halves

    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):  #while the length of both sorted halves are not 0
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])            #append any remaining elements left maybe odd # of elements
    merged.extend(right[right_index:])

    return merged


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)