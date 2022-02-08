# 1번 시계 , -1 반시 / N극 0 S극 1

wheel = []
spin = []

result = 0

for i in range(4):
    numbers = list(input())
    wheel.append(numbers)
print(wheel)

for j in range(int(input())):
    wheelNum , direction = map(int,input().split())
    first = wheel[0][0] ;second = wheel[1][0] ;third = wheel[2][0] ;four = wheel[3][0]
    if(wheelNum == 1):
        print(1)
    elif(wheelNum == 2):
        print(2)
    elif(wheelNum == 3):
        print(3)
    elif(wheelNum == 4):
        print(4)