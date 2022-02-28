# dfs로 풀기!
import sys
sys.setrecursionlimit(10000)

m , n , k =map(int,input().split())

graph = [[0]*n for _ in range(m)]

# x축으로 증가하려면 j값을 움직여야하고 y축으로 증가하려면 i축을 움직여야 한다.
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

print(graph)

# 상하좌우로 움직인다.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

def dfs(x,y):
    global cnt
    # x,y가 범위를 넘거나 1인 상태면 함수를 탈출한다.
    if x<0 or x>=m or y<0 or y>=n:
        return 0
    if graph[x][y] == 1:
        return 0

    # 방문했으면 1로 바꿔준다. 그리고 카운트를 증가시켜준다.
    graph[x][y] = 1
    cnt +=1

    # 4방면을 모두 확인
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        dfs(nx,ny)

    return cnt


result = []
for i in range(m):
    for j in range(n):
        cnt = dfs(i,j)
        if cnt != 0:
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i , end= ' ')

