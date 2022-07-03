from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(place, x, y):
    visited = [[0] * 5 for _ in range(5)]
    queue = deque()
    # 좌표와 cost를 넣을것이다. cost는 맨해튼 거리!
    queue.append([x, y, 0])
    # P인곳은 방문처리한다.
    visited[x][y] = 1

    while queue:
        x, y, cost = queue.popleft()
        if cost == 2:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 만일 이동하는곳이 범위안에 있고 O라면 방문 처리를 하고 비용을 늘린다.
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'P':
                    return False
                if place[nx][ny] == 'O':
                    queue.append([nx, ny , cost+1])
                    visited[nx][ny] = 1
    return True

def solution(places):
    res = []

    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                # P일때 탐색을 시작한다.
                if place[i][j] == 'P':
                    # 거리두기가 지켜지지 않았다면 ( bfs값이 false라면  flag를 False로 바꾼다. )
                    if not bfs(place , i , j):
                        flag = False
        # 만약에 flag가 True면 거리두기가 잘 지켜준거니까 1 아니면 0
        if flag == True:
            res.append(1)
        else:
            res.append(0)
    return res

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])