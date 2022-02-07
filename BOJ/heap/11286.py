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
            popItem = heap[0]
            # 아마 여기서 시간 초과 났을 확률이 높다.
            # 시간 제한은 1초였고 100,000번을 전부돌면서 확인해야하기 때문에
            for i in range(1,len(heap)):
                if(abs(popItem) > abs(heap[i])):
                    popItem = heap[i]
                elif(abs(popItem) < abs(heap[i])):
                    popItem = popItem
                elif(abs(popItem) == abs(heap[i])):
                    if(popItem > heap[i]):
                        popItem = heap[i]
                    else:
                        popItem = popItem
            print(popItem)
            heap.remove(popItem)
    else:
        heapq.heappush(heap , output)
