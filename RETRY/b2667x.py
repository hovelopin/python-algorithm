# 인접행렬 + dfs 문제

'''
내가 dfs 개념을 배울때는 인접리스트 방식으로 구현하는 법을 배웠고 인접행렬로 하려니까 어려움이
있어 대표문제로 뽑고 개념을 공부해봤다.

접근하는 방식은 똑같다 . => 하지만 , 탐색하는 방법을 몰랐음
1. 그래프 입력받고 visited를 만든다.
2. 탐색의 시작점을 찾아서 진행시킨다.
3.
'''


n = int(input())
graph = []
# 그래프를 입력 받음
for _ in range(n):
    graph.append(list(map(int,input())))
visited = [[0]*n for i in range(n)]

result = []
cnt = 0

# 상 , 하 ,좌 , 우
dx = [-1 , 1 ,0 ,0]
dy = [0 , 0 , -1 ,1]

def dfs(x,y):
    global cnt
    # 행렬의 범위를 넘어가면 False
    if x<0 or x >= n or y<0 or y >= n:
        return False

    # 1인곳을 만나면 탐색을 시작해야한다.
    if graph[x][y] == 1:
        cnt+=1
        # 탐색을 했다는 표시 => 인접리스트에서 True로 바꿔주고 출력하는것이랑 같다.
        graph[x][y] = 0
        # ( 탐색한 곳을 기준으로 상하좌우 인접행렬을 탐색한다. )
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx ,ny)
        return True

for i in range(n):
    for j in range(n):
        # visited가 0 이고 graph가 1이라면 탐색을 시작한다.
        if visited[i][j] == 0 and graph[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for i in result:
    print(i)

'''
궁금한 점 
1. 반복문안에 재귀를 돌렸을때 조건에 맞지않으면 다시 반복문으로 ,, 왜?!? ( 인접리스트랑 비교해보기 ) 
'''


