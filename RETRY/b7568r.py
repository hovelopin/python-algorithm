size = []
result = []

# 몸무게와 키를 입력해 리스트에 리스트형태로 넣는다.
for i in range(int(input())):
    x , y = map(int,input().split())
    size.append([x,y])

# 사이즈를 기준으로 하나하나 비교해본다.
for i in range(len(size)):
    cnt = 1
    for j in range(len(size)):
        if(size[i][0] < size[j][0] and size[i][1] < size[j][1]):
            cnt+=1
    result.append(cnt)

# 값을 출력해준다.
for i in result:
    print(i , end=' ')
