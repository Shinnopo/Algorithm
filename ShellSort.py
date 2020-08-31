def sort(data):
    gaps = [7, 3, 1]
    for gap in gaps:
        for i in range(0, len(data), gap):
            for j in range(i-gap, 0, -gap):
                if data[j] > data[j+gap]:
                    data[j], data[j+gap] = data[j+gap], data[j]
                else:
                    break
