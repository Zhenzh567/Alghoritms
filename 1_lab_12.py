def merge(seg1, seg2):
    res = []
    i = j = 0
    while i < len(seg1) and j < len(seg2):
        if seg1[i] <= seg2[j]:
            res.append(seg1[i])
            i += 1
        else:
            res.append(seg2[j])
            j += 1
    while i < len(seg1):
        res.append(seg1[i])
        i += 1
    while j < len(seg2):
        res.append(seg2[j])
        j += 1
    return res


def polyphase_sort(arr, S):
    total = len(arr)
    if total <= 1:
        return arr

    files = {"A": [], "B": [], "C": [], "D": []}

    curr = "A"
    for i in range(0, total, S):
        chunk = sorted(arr[i : i + S])
        files[curr].extend(chunk)
        curr = "B" if curr == "A" else "A"

    size = S
    in1, in2, out = "A", "B", "C"

    while max(len(v) for v in files.values()) < total:
        while len(files[in1]) > 0 or len(files[in2]) > 0:
            seg1 = files[in1][:size]
            files[in1] = files[in1][size:]
            seg2 = files[in2][:size]
            files[in2] = files[in2][size:]

            if not seg1 and not seg2:
                break

            merged = merge(seg1, seg2)
            files[out].extend(merged)

            if out == "A":
                out = "B"
            elif out == "B":
                out = "A"
            elif out == "C":
                out = "D"
            elif out == "D":
                out = "C"

        size *= 2
        if in1 == "A":
            in1, in2, out = "C", "D", "A"
        else:
            in1, in2, out = "A", "B", "C"

    for tape in files.values():
        if len(tape) == total:
            return tape


if __name__ == "__main__":
    data = [12, 4, 1, 9, 20, 5, 11, 2]
    print("Результат:", polyphase_sort(data, S=2))
