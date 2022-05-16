# 19시 25분 ( 시작 ) => 20시 ( 끝 )
# 게임 개발 ( 구현 ) => 해결 못함

n , m = map(int,input().split())

check = [[0]*m for _ in range(n)]

x ,y ,direction = map(int,input().split())
check[x][y] = 1 # 현재 좌표 방문 처리

# 0 : 육지 , 1 : 바다
game = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 여기서는 이 생각이 제일 중요했던 것 같다.
# 왼쪽으로 회전하는 방법을 잘 몰랐는데 좌표를 이용해서 -1에 가게되면 가장 끝 좌표를 가리키게 만드는것이 효과적인 방법이였다.. 나는 if문을 난사했다.
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후에 정면에 가보지 않은 칸이 존재한다면
    # 방문으로 바꾸고 움직인 좌표를 x , y로 바꿔준다. 그리고 값을 1증가시키고 갈수있는 방향을 초기화 시킨다.
    if check[nx][ny] == 0 and game[nx][ny] == 0:
        check[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 이동하기
        if check[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


"""
테스트케이스 1 
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""