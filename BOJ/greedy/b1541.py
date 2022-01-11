# split함수는 list에 담지 않아도 기본적으로 list로 반환한다.

# 입력받은 answer를 -를 기준으로 나눈다.
answer = input().split('-')

solve = []
output = 0

# 반복문을 통해서 문자열로된 '50+40'을 '+'기준으로 split하여서 그 값들을 반복문을 통해서 더해준다.
for i in range(len(answer)):
    result = 0
    arr = answer[i].split('+')
    for j in range(len(arr)):
        result += int(arr[j])
    solve.append(result)

# 첫번째 값을 기준으로 잡고 전부다 빼준다!
output = solve[0]
for k in range(len(solve)-1):
     output -= solve[k+1]

# output값을 출력한다.
print(output)

