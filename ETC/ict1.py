# 12시 10분 시작 => 12시 30분 끝 ( 20분 )
# 큰수의 법칙 ( 그리디 )
n , m , k = map(int,input().split())
nList = list(map(int,input().split()))
result = []
idx = []

maxValue = max(nList)
nList.remove(max(nList))

cnt = 0

for i in range(m):
    if( cnt < k ):
        result.append(maxValue)
        cnt += 1
    else:
        result.append(max(nList))
        cnt = 0
print(sum(result))



'''
테스트 케이스 1
5 8 3
2 4 5 4 6
'''
