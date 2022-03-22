from itertools import permutations

n = int(input())
numList = list(map(int,input().split()))

op = ['+','-','*','/']
oper = list(map(int,input().split()))

opList = []

for i in range(4):
    for j in range(oper[i]):
        opList.append(op[i])

# set을 사용하는 이유가 opList에는 중복되어있는 원소들이 있기 때문에 그것을 배제하기 위해 사용한다!
opList = list(set(permutations(opList , len(opList))))

ans = []

for i in opList:
    start = numList[0]
    for j in range(len(numList)-1):
        if i[j] == '+':
            start += numList[j+1]
        elif i[j] == '-':
            start -= numList[j+1]
        elif i[j] == '*':
            start *= numList[j+1]
        else:
            if start//numList[j+1] < 0:
                start = -(-start//numList[j+1])
            else:
                start = start//numList[j+1]
    ans.append(start)

print(max(ans))
print(min(ans))




