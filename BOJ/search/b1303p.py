# 답은 맞았지만 너무 안좋은 코드다 ,, 수정하자!

n , m = map(int,input().split())

world = [list(input()) for _ in range(m)]

weCnt = 0
otherCnt = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

we = []
other = []

def dfsA(x,y):
    global weCnt
    global otherCnt

    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if world[x][y] == 'W':
        weCnt+=1
        world[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfsA(nx,ny)
        return True
    return False

def dfsB(x,y):
    global otherCnt

    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if world[x][y] == 'B':
        otherCnt+=1
        world[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfsB(nx,ny)
        return True
    return False

for i in range(m):
    for j in range(n):
        if dfsA(i,j) == True:
            we.append(weCnt)
            weCnt = 0

for i in range(m):
    for j in range(n):
        if dfsB(i,j) == True:
            other.append(otherCnt)
            otherCnt = 0

result1 = []
result2 = []

for i in we:
    result1.append(i**2)

for j in other:
    result2.append(j**2)
print(f'{sum(result1)} {sum(result2)}')
