from heapq import heappush, heappop

def sort(data):
    heap = []
    while data:
        heappush(heap, data.pop())
    while heap:
        data.append(heappop(heap))
