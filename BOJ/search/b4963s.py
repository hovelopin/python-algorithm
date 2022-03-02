from collections import deque

def bfs(x,y):
    # 대각선 탐색하는 방법
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    island[x][y] = 0
    # 큐를 다시만들어서 다시 삽입해준다.
    queue = deque()
    queue.append([x,y])
    # queue가 비어있을때까지 반복한다.
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                island[nx][ny] = 0
                queue.append([nx, ny])
while 1:
    # 너비와 높이를 입력받는다.
    w,h = map(int,input().split())
    if ( w == 0 and h == 0 ): break

    island = []
    cnt = 0

    for i in range(h):
        island.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)



