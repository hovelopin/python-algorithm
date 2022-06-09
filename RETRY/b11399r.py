# 20시 42분 ( 시작 ) => 20시 50분 ( 끝 )
n = int(input())
sumCost = 0

# 오름차순 정렬을 시킨다.
cost_time = list(map(int,input().split()))
cost_time.sort()

for i in range(len(cost_time)):
    sumCost += cost_time[i]
    cost_time[i] = sumCost
print(sum(cost_time))


