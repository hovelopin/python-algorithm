# 정답은 맞았지만 시간초과 문제
import sys

while 1:
    cnt = 0
    sum = 0

    n = int(sys.stdin.readline())

    if( n==0 ):
        break
    for i in range(n+1,2*n+1):
        if(i==1):
            sum+=1
            continue
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            sum+=1
    print(sum)
