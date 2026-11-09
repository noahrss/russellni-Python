arr = [3,6,8,11,14,15,18,20,24,27,32]

def linearSearchRecursive(item, arr, n):
    if arr[n-1] == item:
        return n-1
    if n > 0:
        return linearSearchRecursive(item, arr, n - 1)
    return -1

print(linearSearchRecursive(15, arr, len(arr)))