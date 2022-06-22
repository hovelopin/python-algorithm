# 20시 45분 ( 시작 ) =>

n = int(input())
# 1일부터 n일까지 순차적으로 나타남
meeting = [list(map(int,input().split())) for _ in range(n)]

maxProfit = 0

for i in range(n):
    value = 0
    for now in range(0, len(meeting), t):
        t, p = meeting[now]
        if now + t > n-1:
            break
        else:
            value += p
    maxProfit = max(maxProfit , value)
print(maxProfit)







