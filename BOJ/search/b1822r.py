# 23시 18분

a , b = map(int,input().split())
aList = list(map(int,input().split()))
bList = list(map(int,input().split()))

result = []
cnt = 0

# 오름차순으로 정렬
aList.sort()

for i in bList:
    left = 0
    right = len(aList) - 1
    while left <= right:
        mid = (left+right) // 2

        if aList[mid] == i:
            break
        elif aList[mid] < i:
            left = mid + 1
        else:
            right = mid - 1

if len(result) == 0:
    print(0)
else:
    print(cnt)
    for i in result:
        print(i , end = ' ')