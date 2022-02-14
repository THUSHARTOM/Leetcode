import collections


arr = [1, 2, 3, 4, 5, 6, 7]
k = 6
# Sol3

# 1. rotate n-k
# 2. rotate rest
# 3. rotate whole array


def rotate(arr, k):
    n = len(arr)
    k = k % n
    start = 0
    end = n-k-1
    arr = reverse(arr, start, end)
    print(arr)
    arr = reverse(arr, n-k, n-1)
    print(arr)
    arr = reverse(arr, 0, n-1)
    print(arr)


def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array
    # print(array)


rotate(arr, k)
# reverse([1, 2, 3, 4, 5], 2, 4)

# sol2 not O(1)

# n = len(arr)
# k = k % n  # to avoid moving more than len(arr)
# arr[:] = arr[n-k:] + arr[:n-k]
# print(arr)

# sol1

# result = collections.deque(arr)

# result.rotate((k))

# arr = list(result)
# print(arr)
