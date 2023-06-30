size = int(input("Enter size: "))
arr = list(map(int, input("Enter elements of array: ").split()))
swaps = 0

for i in range(size):
    swapped = False

    #upper bound is size - i - 1 because on every iteration, the last item should be in its place so no need to iterate
    for j in range(size - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
            swapped = True

        if not swapped:
            break
print("the number of swaps are: ", swaps)

print(arr)
