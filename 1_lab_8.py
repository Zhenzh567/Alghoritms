def radix_sort(arr):
    if not arr:
        return arr

    negatives = [num for num in arr if num < 0]
    positives = [num for num in arr if num >= 0]

    def sort_non_negative(sub_arr):
        if not sub_arr:
            return sub_arr
        
        max_num = max(sub_arr)
        exp = 1
        while max_num // exp > 0:
            buckets = [[] for _ in range(10)]
            for num in sub_arr:
                digit = (num // exp) % 10
                buckets[digit].append(num)
            sub_arr = [num for bucket in buckets for num in bucket]
            exp *= 10
        return sub_arr

    sorted_positives = sort_non_negative(positives)

    absolute_negatives = [abs(num) for num in negatives]
    sorted_abs_negatives = sort_non_negative(absolute_negatives)
    sorted_negatives = [-num for num in reversed(sorted_abs_negatives)]

    return sorted_negatives + sorted_positives
