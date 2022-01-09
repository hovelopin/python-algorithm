# 간단한 문제인데 zero division 에러가 떴었음

a,b,c = map(int,input().split())

if(b>=c):
    print(-1)
else:
    print(int(a / (c - b))+1)
