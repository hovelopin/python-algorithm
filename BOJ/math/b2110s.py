# 12시 30분 시작
import sys

# n 집의 개수  , c 공유기 개수
n , c = map(int,sys.stdin.readline().split())
xList = [int(sys.stdin.readline()) for _ in range(n)]
xList.sort() # 오름차순 정렬

result = []


# index
mid = xList[len(xList)//2]

while c>0:
    result.append(mid)
    if (xList[-1] - mid) >= (mid - xList[0]):
        mid = xList[-1]
    else:
        mid = xList[0]
    c -= 1

result.sort()

resultValue = 9999999

for i in range(len(result) - 1):
    if (result[i+1] - result[i]) < resultValue:
        value = result[i+1] - result[i]
        resultValue = value
    else:
        value = resultValue
print(resultValue)

