from collections import deque

n , m = map(int,input().split())
paint = []

for _ in range(n):
    paint.append(list(map(int,input().split())))

paintCnt = 0
paintWidth = 0

maxWidth =[]
maxCnt = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(x,y):
    global paintWidth
    queue = deque()
    queue.append([x,y])
    # 처음 탐색했으면 0으로 만들고 paintWidth도 0이다.
    paint[x][y] = 0
    paintWidth += 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if( 0<= nx <n and 0<= ny < m and paint[nx][ny] == 1):
                paint[nx][ny] = 0
                queue.append([nx,ny])
                paintWidth+=1

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1:
            bfs(i,j)
            if(paintWidth != 0):
                maxWidth.append(paintWidth)
            paintCnt+=1
            paintWidth = 0


if(len(maxWidth) == 0):
    print(paintCnt)
    print(0)
else:
    print(paintCnt)
    print(max(maxWidth))


