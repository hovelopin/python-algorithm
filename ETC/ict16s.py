# 19시 25분 ( 시작 ) => 20시 ( 끝 )
# 게임 개발 ( 구현 ) => 해결 못함
from collections import deque

n , m = map(int,input().split())
# 현재 좌표와 방향
# 북 : 0 , 동 : 1 , 남 : 2 , 서 : 3
coor_x ,coor_y ,direction = map(int,input().split())
# 0 : 육지 , 1 : 바다
game = [list(map(int,input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]

answer = 0

# 반시계 방향으로 돈다.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
        x, y = queue.popleft()
        # 북 , 동 , 남 , 서 순으로 체크
        if direction == 0:
            nx = x + dx[0]
            ny = y + dy[0]
        elif direction == 1:
            nx = x + dx[3]
            ny = y + dy[3]
        elif direction == 2:
            nx = x + dx[1]
            ny = y + dy[1]
        else:
            nx = x + dx[2]
            ny = y + dy[2]

        # 범위를 벗어나지 않았고 건너지 않았다면
        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0:
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 1
            else:
                direction = 2








bfs(coor_x , coor_y)






