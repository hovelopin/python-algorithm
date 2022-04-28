# 22시 25분 ( 시작 ) => 22시 30분 ( 끝 ) =====> 5분
# 1이 될 때까지 ( 그리디 )

n , k = map(int,input().split())
cnt = 0

while n != 1:
    if(n%k == 0) : n = n // k
    else:
        n-=1
    cnt+=1
print(cnt)

'''
테스트 케이스 1
25 5
'''