# k번째 수 찾기 ( 입력된 숫자들 중에서 k번째로 작은 수를 반환하시오 )
n , k = map(int,input().split())
result = []
data = []
nList = list(map(int,input().split()))

for el in nList:
    data.append(el)
    data.sort()
    if len(data) < k:
        result.append(-1)
    else:
        result.append(data[k-1])
print(*result)



