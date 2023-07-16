def insertion_sort(bucket):
    for i in range(len(bucket)):
        temp = bucket[i]
        j = i

        while j > 0 and temp < bucket[j - 1]:
            bucket[j] = bucket[j-1]
            j -= 1

        bucket[j] = temp


def bucket_sort(arr):
    num_buckets = len(arr)  # determine the number of buckets
    buckets = [[] for _ in range(num_buckets)]  # create empty buckets

    max_val = max(arr)      # find max val in the array

    for i in range(len(arr)):   # scale input elements to fit within range of 0 to 1
        arr[i] = arr[i] / max_val

    for num in arr:         # distribute elements into buckets
        index = int(num * (num_buckets - 1))
        buckets[index].append(num)

    for bucket in buckets:      # sort individual buckets
        insertion_sort(bucket)

    sorted_arr = []             # concatenate sorted buckets
    for bucket in buckets:
        sorted_arr.extend(bucket)

    for i in range(len(sorted_arr)):    # elements are rescaled back to original range
        sorted_arr[i] = sorted_arr[i] * max_val

    return sorted_arr


arr = [5, 2, 4, 6, 5.1 , 10]
sorted_arr = bucket_sort(arr)
print(sorted_arr)

