# 22시 55분 ( 시작 ) =>  23시 45분 ( 끝 ) =====>  50분
# 만들 수 없는 금액 ( 구현 )

n = int(input())
nList = list(map(int,input().split()))
nList.sort()

target = 1

for i in nList:
    if target < i:
        break
    target += i
print(target)


"""
테스트케이스 1
5
3 2 1 1 9
"""
