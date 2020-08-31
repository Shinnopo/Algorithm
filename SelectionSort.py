def sort(data):
    for i in range(0, len(data)-1):
        min_i = i
        for j in range(i+1, len(data)):
            if data[min_i] > data[j]:
                min_i = j
        data[min_i], data[i] = data[i], data[min_i]
