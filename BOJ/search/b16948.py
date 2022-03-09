# 21시 53분 ==> 22시 10분 끝 ( 17분 )

from collections import deque

# (-2,-1) , (-2 , +1 ) , (0, -2) , (0,+2) , (2,-1) , (2,1)
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

N = int(input())

r1 , c1 , r2 , c2 = map(int,input().split())

chase = [[0] * N for _ in range(N)]
cnt = 0

def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        if (x == r2 and y == c2):
            print(chase[r2][c2])
            exit()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and chase[nx][ny] == 0:
                chase[nx][ny] = chase[x][y] + 1
                queue.append([nx,ny])
    if (chase[r2][c2] == 0):
        print(-1)
bfs(r1,c1)