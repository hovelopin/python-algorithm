# N개의 수를 입력받는다.
N = int(input())

# 시간순으로 오름차순으로 정렬을한다.
time = sorted(list(map(int,input().split())))
result = 0

# slice를 이용해서 sum값을 더해준다!!
for i in range(1, len(time)+1):
    result += sum(time[0:i])
print(result)