# 21시 25분 (시작) => 21시 40분 (끝) => 15분
h, w = map(int,input().split())

joi = [list(input()) for _ in range(h)]

def checked(joi , height , start):
    if start == w-1:
        return
    for i in range(start+1, w):
        if joi[height][i] == 'c':
            return
        joi[height][i] = joi[height][i-1] + 1

for i in range(h):
    for j in range(w):
        if joi[i][j] == 'c':
            joi[i][j] = 0
            checked(joi,i,j)
        elif joi[i][j] == '.':
            joi[i][j] = -1

for i in joi:
    print(*i, end=" ")
    print()
