def search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
print("要素番号{}にデータ{}を見つけました。".format(search(data, target), target))
