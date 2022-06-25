# 23시 20분 ( 시작 ) => 23시 29분 ( 끝 )
"""
5킬로 , 3킬로
"""
import math

n = int(input())
minValue = math.inf

downCount = n // 5
for i in range(downCount , -1 , -1):
    if (n-5*i) % 3 == 0:
        upCount = (n-5*i) // 3
        cnt = i + upCount
        minValue = min(cnt, minValue)

if minValue == math.inf:
    print(-1)
else:
    print(minValue)
