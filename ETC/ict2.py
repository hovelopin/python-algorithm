# 22시 5분 (시작) => 22시 17분 ( 끝 ) ====> 약 12분 소요
# 숫자 카드 게임 ( 그리디 )

n , m = map (int,input().split())
nList = [list(map(int,input().split())) for _ in range(n)]
minNList = []

for i in nList:
    minNList.append(min(i))

print(max(minNList))

'''
테스트 케이스 1
3 3
3 1 2 
4 1 4
2 2 2

테스트 케이스 2
2 4
7 3 1 8
3 3 3 4
'''