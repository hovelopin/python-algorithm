import sys

n = int(sys.stdin.readline())
nList = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))

nList.sort()

for i in mList:
    left = 0
    right = len(nList) - 1

    while left <= right:
        mid = (left+right) // 2
        if nList[mid] == i:
            print(1, end= ' ')
            break
        elif nList[mid] < i:
            left = mid + 1
        else:
            right = mid - 1
    if nList[mid] == i:
        continue
    else:
        print(0 , end= ' ')
