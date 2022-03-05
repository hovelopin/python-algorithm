'''
최단거리를 구하는 것임
=> 값을 한개씩 늘려갈건데 기본적으로 pop했을때의 값을 기준으로 + 1해주는거 그래서
첫번째 예제에서 (0,5)랑 (1,4)가 똑같은 값을 가진다.
'''

from collections import deque

N,M = map(int,input().split())

miro = [list(map(int,input())) for _ in range(N)]

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue=deque()
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1):
                queue.append([nx,ny])
                miro[nx][ny] = miro[x][y]+1
    return miro[N-1][M-1]
print(bfs(0,0))



