n = int(input())

candy = [list(map(str,input())) for _ in range(n)]

maxCnt = 0

dx = [1,0]
dy = [0,1]

def change(x,y,candy):
    # 2번만 바꿀꺼니까!
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<n and ny<n:
            if candy[x][y] != candy[nx][ny]:
                candy[x][y] , candy[nx][ny] = candy[nx][ny] , candy[x][y]
                check(candy)
                candy[x][y] , candy[nx][ny] = candy[nx][ny] , candy[x][y]
            if maxCnt == n:
                return


def check(candy):
    global maxCnt
    result = 1
    for i in range(n):
        row = 1
        col = 1
        for j in range(1,n):
            if candy[i][j] == candy[i][j-1]:
                row += 1
            else: row = 1

            if candy[j][i] == candy[j-1][i]:
                col+=1
            else: col = 1

            result = max(row,col,result)
    maxCnt = max(result,maxCnt)

# c,p,z,y
for i in range(n):
    for j in range(n):
        change(i,j,candy)
    if maxCnt == n:
        break

print(maxCnt)

