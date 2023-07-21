def count_sort(arr):
    max_val = max(arr)              # find max element in array to determine range
    count = [0] * (max_val + 1)     # create counting array to store the count of each element
    for num in arr:                 # count occurrences of each element in input array
        count[num] += 1

    for i in range(1, len(count)):  # calculate cumulative count of each element in the counting array
        count[i] += count[i+1]

    output = [0] * len(arr)         # create output array to store the sorted elements
    for num in arr:                 # place elements in sorted order based on count array
        output[count[num] - 1] = num
        count[num] -= 1

    return output
