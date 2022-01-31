rectangle_x = []
rectangle_y = []

for i in range(3):
    x,y = map(int,input().split())
    rectangle_x.append(x)
    rectangle_y.append(y)

for i in range(3):
    if(rectangle_x.count(rectangle_x[i]) == 1):
        result_x = rectangle_x[i]
    if (rectangle_y.count(rectangle_y[i]) == 1):
        result_y = rectangle_y[i]

print(f'{result_x} {result_y}')

