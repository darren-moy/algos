def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        temp = arr[i]       #storing current element whose left side is checked for its correct position
        j = i

        while (j > 0 and temp < arr[j - 1]):    #check whether adjacent element on left side is >= current element
            arr[j] = arr[j-1]                   #move left side element to one position forward
            j = j - 1

        arr[j] = temp



arr = [5, 3, 8, 2, 1]
insertion_sort(arr)
print(arr)