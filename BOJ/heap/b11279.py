import heapq ,sys

heap = []

numbers = int(sys.stdin.readline())

for i in range(numbers):
    command = int(sys.stdin.readline())
    if(command == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap , (-command , command))
