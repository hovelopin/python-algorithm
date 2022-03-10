# 22시 21분 =>
N, M , L = map(int,input().split())

cnt = 1
# 1번부터 n번까지
result = [0]*N

start = 0

while 1:
    result[start] += 1
    if(max(result) == M):
        break
    if(result[start] < M ):
        if(result[start]%2 == 1):
            if(start <= N-1):
                start += L
            else:
                start = start % M
        else:
            if(start < -M ):
                start = (-start) % M
                start = (-start)
            else:
                start -= L
    cnt+=1
print(cnt)