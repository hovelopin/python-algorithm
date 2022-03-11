# 13시 55분 시작
N , M = map(int,input().split())

number = [1] * M


for i in range(-1,-(M+1),-1):
    for j in range(N):
        for k in number:
            print(k, end=' ')
            print()
        number[i] += 1
    number = [1] * M



