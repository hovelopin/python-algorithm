# 다시풀었는데 못푼문제.. 틀린이유 정확하게 분석하자!

command = input().upper()

# 중복을 제거하고 리스트에 넣기 set함수는 중복을 제거하지만 순서는 상관이 없음
newCommand = list(set(command))

output = []

for i in newCommand:
    cnt = command.count(i)
    output.append(cnt)

# count를 이용해서 최대값이 2개 이상이면 '?'를 사용한다.
if(output.count(max(output)) > 1):
    print('?')
else:
    maxIndex = output.index(max(output))
    print(newCommand[maxIndex])


