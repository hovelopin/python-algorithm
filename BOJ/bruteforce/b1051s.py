n , m =map(int,input().split())

square = [list(map(int,input())) for _ in range(n)]

d = min(n,m)

ans = 1

for i in range(n):
    for j in range(m):
        for k in range(1,d):
            # 최대로 갈 수 있는 범위 안에 있으면 그 값을 temp에 넣는다.
            # 그리고 temp랑 , k만큼 떨어진 좌표들의 값이랑 같으면 그 값을 ans에 저장한다.
            if i+k < n and j+k < m:
                temp = square[i][j]
                if temp == square[i+k][j] and temp == square[i][j+k] and square[i+k][j+k]:
                    ans = max(ans , (k+1)**2)
print(ans)

