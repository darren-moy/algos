def partition(arr, start, end):  # array start and end
    pivot = arr[end]  # last element as pivot
    i = start - 1  # index of the smallest element

    for j in range(start, end):
        if arr[j] <= pivot:  # elements that are smaller go to the left of the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # put value at j in place at index i

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1  # index of the pivot


def quick_sort(arr, start, end):
    if start < end:  # checks if there are at least 2 elements otherwise sorted
        pivot_index = partition(arr, start, end)  # will return the pivot index

        quick_sort(arr, start, pivot_index - 1)  # recursive call on left side of pivot
        quick_sort(arr, pivot_index + 1, end)  # recursive call on right side of pivot


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print(arr)
