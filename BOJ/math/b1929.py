# 문제는 맞았지만 시간초과 나온다.
import sys

M , N = map(int,sys.stdin.readline().split())

K = M # K값을 이용해서 M을 한칸씩 늘려가며 범위를 구하기 위해서

for i in range(M,N+1):
    K += 1
    cnt = 0
    for j in range(2,K):
        if(i%j==0):
            cnt+=1
        if(cnt>2):
            break
    if(cnt == 1):
        print(i)