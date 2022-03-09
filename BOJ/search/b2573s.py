from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


def bfs(x, y, ice, check):
    queue = deque()
    queue.append([x, y])
    check[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] != 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append([nx, ny])


def melting(x, y, ice, check):
    check[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0 and ice[x][y] > 0 and check[nx][ny] == 0:
            ice[x][y] -= 1

    if check[x][y] > 0:
        return 1
    else:
        return 0


N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

year = 0

while 1:
    # 빙산 녹이기
    flag = 0
    check = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                # bfs 탐색!
                if (melting(i, j, ice, check)):
                    flag = 1
    # 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.
    if flag == 0:
        year = 0
        break

    check = [[0 for i in range(M)] for j in range(N)]
    cnt = 0

    # 빙산 덩이 확인
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0 and ice[i][j] != 0:
                bfs(i, j, ice, check)
                cnt += 1
    if cnt >= 2:
        year += 1
        break
    else:
        year += 1

print(year)