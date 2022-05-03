# 23시 40분 ( 시작 ) =>  24시 ( 끝 ) =====>  20분
# 모험가의 길드 ( 그리디 )
n = int(input())
fear = list(map(int,input().split()))
# 오름차순 정렬
fear.sort()
member = 0
sumResult = 0

for i in fear:
    member += 1
    if member >= i :
        sumResult += 1
        member = 0
print(sumResult)




"""
테스트 케이스 1
5
2 3 1 2 2
"""
