def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        minimum_idx = i

        # Find the index of the minimum element in the remaining unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[minimum_idx]:
                minimum_idx = j

        # Swap the minimum element with the current element
        arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]


# Example usage:
arr = [5, 3, 8, 2, 1]
selection_sort(arr)
print(arr)