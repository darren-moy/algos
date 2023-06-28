def bubble_sort(arr):
    size = len(arr)
    count = 0
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1

    return count, arr


#def selection_sort(arr):
