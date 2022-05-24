def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1
    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr.extend(count * [i])

    return sorted_arr


arr = [9, 4, 7, 2, 5, 3, 6, 1, 2]
k = max(arr) + 1

print(bucketsort(arr, k))
