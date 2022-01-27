# start에서 end까지의 범위로 입력받는다.
start , end = map(int,input().split())

# 첫번째는 1개 2번째는 2개 3번째는 3개 n번째는 n개
cnt = 1
# 1부터 시작할 것이고
num = 1
# 결과를 리스트에 넣으면 된다.
result = []

# 리스트의 결과의 길이가 end보다 작으면 반복문을 탈출했습니다.
while len(result) < end:
    # num을 cnt번 곱한것을 number라고 하고 그 값을 result에 extend를 이용해서 배열을 이어준다.
    number = [num]*cnt
    result.extend(number)

    cnt+=1
    num+=1

print(result)
print(sum(result[start-1:end]))
