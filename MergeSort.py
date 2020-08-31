def sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = sort(data[:mid])
    right = sort(data[mid:])

    merge, l, r = [], 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merge.append(left[r])
            l += 1
        else:
            merge.append(right[r])
            r += 1
    if l < len(left):
        merge.extend(left[l:])
    elif r < len(right):
        merge.extend(right[r:])
    return merge
