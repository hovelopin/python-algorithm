n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

m, k = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

ans = [[0]*n for _ in range(k)]

for n in range(n):
    for k in range(k):
        for m in range(m):
            ans[n][k] += a[n][m] * b[m][k]

for i in ans:
    for j in i:
        print(j, end=' ')
    print()

