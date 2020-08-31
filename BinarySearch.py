def search(data, target):
    start, end = 0, len(data)
    while start <= end:
        i = (start + end) // 2
        if data[i] == target:
            return i
        elif data[i] < target:
            start = i + 1
        else:
            end = i - 1
    return -1
