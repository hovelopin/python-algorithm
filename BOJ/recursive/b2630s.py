# 16시35분 시작 => 20분

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

white = 0 # 0으로 주어진다.
blue = 0 # 1로 주어진다.


def cut(x,y,n):
    global white , blue

    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                cut(x, y , n//2)
                cut(x, y+n//2 , n//2)
                cut(x+n//2 , y , n//2)
                cut(x+n//2 , y+n//2 , n//2)
                return
    if check == 0:
        white += 1
    else:
        blue += 1


cut(0,0,n)
print(white)
print(blue)
