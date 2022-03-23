# 시작 : 18시 35분
# 끝 : 18시 45분  => 10분

a , b = map(int,input().split())
aList = list(map(int,input().split()))
bList = list(map(int,input().split()))

set1 = set(aList)
set2 = set(bList)

resultSet = list(set1-set2)
resultSet.sort()

if len(resultSet) == 0:
    print(0)
else:
    print(len(resultSet))
    for i in resultSet:
        print(i , end = ' ')



