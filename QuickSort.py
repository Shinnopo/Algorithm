def sort(data):
    n = len(data)
    pivot = data[n//2]
    left, right, middle = [], [], []
    for i in range(n):
        if data[i] < pivot:
            left.append(data[i])
        elif data[i] > pivot:
            right.append(data[i])
        else:
            middle.append(data[i])
    if left:
        left = sort(left)
    if right:
        right = sort(right)
    return left + middle + right
