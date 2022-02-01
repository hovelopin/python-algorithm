rectangle_x = []
rectangle_y = []

# x좌표는 x에 y좌표는 y에 삽입한다.
for i in range(3):
    x,y = map(int,input().split())
    rectangle_x.append(x)
    rectangle_y.append(y)

# x,y좌표중에서 갯수가 1개인것이 있으면 그것을 result에 넣고 출력한다.
for i in range(3):
    if(rectangle_x.count(rectangle_x[i]) == 1):
        result_x = rectangle_x[i]
    if (rectangle_y.count(rectangle_y[i]) == 1):
        result_y = rectangle_y[i]

print(f'{result_x} {result_y}')

