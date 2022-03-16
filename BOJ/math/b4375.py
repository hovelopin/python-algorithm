import sys

while 1:
    num = 1
    a = sys.stdin.readline()
    if(a == ''):
        break
    else:
        while 1:
            if( int(num) % int(a) == 0 ):
                print(len(str(num)))
                break
            else:
                num = str(num)+'1'


