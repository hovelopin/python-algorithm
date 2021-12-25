# 정답은 맞았지만 시간 초과 에러!
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sosu = []
cnt = 0

for i in range(M,N+1):
    cnt = 0
    for j in range(i,1,-1):
        if(i%j==0):
            cnt+=1
    if(cnt==1):
        sosu.append(i)

if(len(sosu)>0):
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
