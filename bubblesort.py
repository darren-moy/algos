def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        #upper bound is size - i - 1 because on every iteration, the last item should be in its place so no need to iterate
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:                       #swap if current item is greater than the item to the right (pushing greatest int to the right)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

arr = [6, 2, 4, 1, 5]
x = bubble_sort(arr)
print(x)

