# 19시 50분 ( 시작 ) => 19시 56분 ( 끝 )
# 볼링공 고르기 ( 그리디 )
n , m = map(int,input().split())
nList = list(map(int,input().split()))

cnt = 0

for i in range(n):
    for j in range(i,n):
        if(nList[i] != nList[j]):
            cnt += 1
print(cnt)

"""
테스트케이스 1
5 3
1 3 2 3 2

테스트케이스 2
8 5 
1 5 4 3 2 4 5 2 

"""
