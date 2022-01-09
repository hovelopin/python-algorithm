import math

while 1:
    x,y,z = map(int,input().split())
    if(x==0 and y==0 and z==0):
        break
    if(math.sqrt(x**2+y**2) == math.sqrt(z**2) or math.sqrt(x**2+z**2) == math.sqrt(y**2) or math.sqrt(z**2+y**2) == math.sqrt(x**2)):
        print("right")
    else:
        print("wrong")
