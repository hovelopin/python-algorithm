# 16시 18분 시작 ==> 38분 종료
import sys
sys.setrecursionlimit(100000)

N = int(input())
graph = []
result = 0

# 상하좌우 배열
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [ [0]*N for i in range(N)]

for i in range(N):
    water = list(map(int,input().split()))
    graph.append(water)

# N보다 작은곳은 전부다 0으로 만들어 놓는다.
def DFS(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if visited[nx][ny]:
            continue
        DFS(nx, ny)

answer = 0
height = 0

while height <= 100:
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= height:
                visited[i][j] = True
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                DFS(i,j)
                cnt+=1

    answer = max(answer,cnt)
    height += 1
    visited = [[0] * N for i in range(N)]
print(answer)
