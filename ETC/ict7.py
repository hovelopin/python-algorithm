from collections import deque

n , m = map(int,input().split())
ice = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    ice[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0):
                queue.append([nx,ny])
                ice[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if(ice[i][j] == 0):
            bfs(i,j)
            cnt+=1
print(cnt)

'''
테스트케이스 1

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

'''