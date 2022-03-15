# https://tmdrl5779.tistory.com/103
# https://chaewsscode.tistory.com/96


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

oneCnt = 0
zeroCnt = 0
minusOneCnt = 0

def recursive(x,y,n):
    global oneCnt , zeroCnt , minusOneCnt

    check = graph[x][y]
    for i in range(x , x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                # 1, 2 ,3
                recursive(x, y, n // 3)
                recursive(x, y +n // 3, n // 3)
                recursive(x, y +n // 3 * 2, n // 3)
                recursive(x+n // 3, y, n // 3)
                # 4, 5 ,6
                recursive(x + n // 3, y + n // 3, n // 3)
                recursive(x + n // 3, y + n // 3 * 2, n // 3)
                recursive(x + n // 3 * 2, y, n // 3)
                # 7, 8, 9
                recursive(x + n // 3 * 2, y + n // 3, n // 3)
                recursive(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return

    if check == 1:
        oneCnt += 1
    elif check == 0:
        zeroCnt += 1
    else:
        minusOneCnt += 1

recursive(0,0,N)

print(minusOneCnt)
print(zeroCnt)
print(oneCnt)



