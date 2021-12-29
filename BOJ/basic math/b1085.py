x,y,w,h = map(int,input().split())

min_x = 0
min_y = 0

if(x-0 > w-x):
    min_x = w - x
else:
    min_x = x - 0

if(y-0 > h-y):
    min_y = h - y
else:
    min_y = y - 0

if(min_x > min_y):
    print(min_y)
else:
    print(min_x)