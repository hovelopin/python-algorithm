# 시작 : 16시 시작 (45분)
# 끝 :

# 0은 빈칸 1은 집 2는 치킨집

from itertools import combinations

n , m = map(int,input().split())

road = [list(map(int,input().split())) for _ in range(n)]

chicken = []
house = []

answer = []

# 치킨과 집의 정보를 담는다.
for i in range(n):
    for j in range(n):
        if(road[i][j] == 1):
            house.append([i,j])
        elif(road[i][j] == 2):
            chicken.append([i,j])

# 이제 최소값을 구함
for ch in combinations(chicken,m):
    total = 0
    for x,y in house:
        Min = 100001
        for x1,y1 in ch:
            dist = abs(x-x1) + abs(y-y1)
            Min = min(Min,dist)
        total+=Min
    answer.append(total)
print(min(answer))
