# 문제는 맞았지만 시간초과 문제
import heapq , sys

heap = []

count = int(sys.stdin.readline())

for i in range(count):
    output = int(sys.stdin.readline())
    if(output == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap , (abs(output),output))
