# 22시 40분 ( 시작 ) =>  22시 55분 ( 끝 ) =====> 15분
# 상하좌우 ( 구현 )
n = int(input())
dirList = list(input().split())

# U , D , L , R
dx = [-1 , 1 ,0 ,0]
dy = [0 , 0 , -1 ,1]

start_x = 0
start_y = 0

for i in dirList:
    if( i == 'U' ):
        if( 0 <= start_x + dx[0] < n and 0 <= start_y + dy[0] < n):
            start_x += dx[0]
            start_y += dy[0]
    elif ( i == 'D'):
        if (0 <= start_x + dx[1] < n and 0 <= start_y + dy[1] < n):
            start_x += dx[1]
            start_y += dy[1]
    elif( i == 'L'):
        if (0 <= start_x + dx[2] < n and 0 <= start_y + dy[2] < n):
            start_x += dx[2]
            start_y += dy[2]
    else:
        if (0 <= start_x + dx[3] < n and 0 <= start_y + dy[3] < n):
            start_x += dx[3]
            start_y += dy[3]
print(start_x+1 , start_y+1)


'''
테스트 케이스1
5
R R R U D D
'''
