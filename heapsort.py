def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:       # check if left child exists and is greater than current root
        largest = left

    if right < n and arr[right] > arr[largest]:     # check if right child exists and is greater than current root
        largest = right

    if largest != i:                                # swap root with largest element if needed
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):     # build a max heap by rearranging array
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):           # extract elements from the heap 1 by 1 and place them at the end
        arr[i], arr[0] = arr[0], arr[i]     # swap the root with the last element
        heapify(arr, i, 0)                  # heapify the reduced heap

    return arr


arr = [10, 7, 8, 9, 1, 5]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)
