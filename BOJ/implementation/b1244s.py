# 21시 4분 =>
# 삼항연산자

switchCnt = int(input())
switch = [300] + list(map(int,input().split()))
student = int(input())

# 1은 남학생 2는 여학생
for i in range(student):
    sex , number = map(int,input().split())

    # 남학생인 경우
    if(sex == 1):
        idx = number
        while idx <= switchCnt :
            switch[idx] = 1 if switch[idx] == 0 else 0
            idx += number
    # 여학생인 경우
    else:
        # 만약 첨부터 양쪽이 다를 경우에 number값을 가진 여학생의 switch는 바꿔줘야 하기 때문에 switchList에 넣는다
        switch[number] = 1 if switch[number] == 0 else 0
        start  = number - 1
        end = number + 1

        while start >= 1 and end <= switchCnt:
            if(switch[start] == switch[end]):
                if(switch[start] == 0):
                    switch[start] = 1
                    switch[end] = 1
                else:
                    switch[start] = 0
                    switch[end] = 0
            else:
                break
            start -= 1
            end += 1
    # print(switch)
for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if not i % 20:
        print()


