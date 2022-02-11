# 탐색문제 => dfs를 써야할지 bfs를 써야할지 정해야 하는데 문제에 인접한 토마토를 익어가는 거라 BFS로 결정
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(N)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

BFS()

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)