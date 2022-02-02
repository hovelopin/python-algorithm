'''
정답은 맞았지만 어거지로 푼 느낌 ,, 코드가 깔끔하지 못하다
'''
num = int(input())

cycle = 0

# 입력받은 num을 new에 넣고
new = num

while 1:
    # 몫과 나머지를 구하고
    first = int(new) // 10
    second = int(new) % 10

    # 두개를 더하고 그거에 대한 나머지랑 위에서 구한 나머지랑 더한다
    result = first + second
    result = result % 10

    new = str(second) + str(result)
    cycle+=1

    # 분리하고 합쳐서 처음 num과 같으면 break로 탈출시킨다.
    if(int(new) == num):
        break
print(cycle)



