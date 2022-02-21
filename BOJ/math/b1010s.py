# 조합 라이브러리를 이용했을때 시간초과난 문제 마지막 케이스를 구할때 리스트가 너무 커짐

T = int(input())

for i in range(T):


    n,m = map(int,input().split())

    # 조합으로 풀건데 west가 0이면 전부다 1이다.
    if n == 0:
        print(0)
        continue

    cnt = 1

    for i in range(n):
        cnt = cnt * (m-i)
    for j in range(1,n+1):
        cnt = cnt//j
    print(cnt)



