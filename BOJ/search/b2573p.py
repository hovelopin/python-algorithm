n , m = map(int,input().split())

ice = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

changeIce = ice

def dfs(x,y):
    ice[x][y] -= 1




for i in range(n):
    for j in range(m):
        if not dfs(i,j):
            cnt += 1

