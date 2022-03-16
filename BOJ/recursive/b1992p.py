n = int(input())

video = [list(map(int,input())) for _ in range(n)]
output = []

def quad(x,y,n):
    # 모두 같은지 확인하기 위해 check 변수
    check = video[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            # 같지 않을때 재귀돌아야 함
            if check != video[i][j]:
                # 1,2,3,4분면을 반복해서 돌꺼임
                quad(x, y, n // 2)
                quad(x, y + n//2 , n // 2)
                quad(x+n//2, y, n // 2)
                quad(x+n//2, y+n//2, n // 2)

    if check == 0:
        output.append(check)
    else:
        output.append(check)

quad(0,0,n)
print(output)