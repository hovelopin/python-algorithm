# 시간초과는 안떴지만 런타임 시간이 오래 걸린 문제
N = int(input())

num = 2

while N>1 :
    if (N%num==0):
        N = N//num
        print(num)
        continue
    num+=1





