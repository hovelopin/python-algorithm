# 21시 37분 ( 시작 ) => 21시 46분 ( 끝 )
# 미로 탈출 ( BFS/DFS )
from collections import deque

n , m = map(int, input().split())
miro = [list(map(int,input())) for _ in range(n)]

dx = [-1 , 1 , 0 , 0]
dy = [0 , 0 , -1 , 1]

cnt = 0
def miro_bfs(x,y):
    global cnt
    queue = deque()
    queue.append([x,y])
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append([nx , ny])
miro_bfs(0 , 0)
print(miro[n-1][m-1])

"""
테스트케이스 1 )
5 6
101010
111111
000001
111111
111111
"""