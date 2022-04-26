n , m , k = map(int,input().split())
nList = list(map(int,input().split()))

# 정렬 , 가장 큰값과 작은값을 저장
nList.sort()
first = nList[n-1]
second = nList[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
