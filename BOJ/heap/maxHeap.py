import heapq

heap = []

for i in range(7):
    item = int(input())
    heapq.heappush(heap , (-item , item))

print(heap)
print(heapq.heappop(heap)[1]) # 7
print(heapq.heappop(heap)[1]) # 6
print(heapq.heappop(heap)[1]) # 5
print(heapq.heappop(heap)[1]) # 4
print(heapq.heappop(heap)[1]) # 3
print(heapq.heappop(heap)[1]) # 2
print(heapq.heappop(heap)[1]) # 1