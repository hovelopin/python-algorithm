# 내 생각 : 제일 비용이 낮은곳에서 최대한 많이사서 나간다!
# 만일 첫번째 주유소가 두번째 주유소보다 크면 두번째 주유소 갈만큼만 산다.
# 도착한 주유소가 가장 비용이 작은 주유소면 남은거 다 산다!

# 서브태스크 2,3번을 다시보자!!
import sys


N = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split())) # [2,3,1]
oil_cost = list(map(int,sys.stdin.readline().split())) # [5,2,4,1]

result = 0

# 마지막 주유 장소는 뺀다.
oil_cost.pop()

# 가장 마지막은 비교하지 않음
for i in range(len(oil_cost)):
    if(oil_cost[i] == min(oil_cost)):
        result += oil_cost[i] * sum(road[i:])
        break
    else:
        result = road[i] * oil_cost[i]

print(result)