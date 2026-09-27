def shell_sort(arr):
    n = len(arr)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            key = arr[i]
            j = i
            while j >= step and arr[j - step] > key:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = key
        step //= 2
    return arr
