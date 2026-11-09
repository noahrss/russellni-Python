arr = [3, 6, 8, 11, 14, 15, 18, 20, 24, 27, 32]

def binarySearch(item, arr):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        mid = (lower + (upper - lower)) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1

print(binarySearch(15, arr))


def binarySearchRecursive(item, arr, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + (upper - lower)) // 2
    if arr[mid] == item:
        return mid
    if arr[mid] > item:
        return binarySearchRecursive(item, arr, lower, mid - 1)
    else:
        return binarySearchRecursive(item, arr, mid + 1, upper)

print(binarySearchRecursive(15, arr, 0, len(arr) - 1))