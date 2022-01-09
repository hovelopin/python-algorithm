x_list = []
y_list = []

new_x = 0 ; new_y = 0

for i in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if(x_list.count(x_list[j]) == 1):
        new_x = x_list[j]
    if(y_list.count(y_list[j]) == 1):
        new_y = y_list[j]
print(new_x , new_y)









