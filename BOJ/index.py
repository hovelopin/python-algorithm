cnt = 0

def dfs(graph , n1 , n2):
    global cnt
    cnt += 1
    visited[n1] = 1

    # 인접하지 않은 곳을 방문하는데 방문 안했으면 재귀로 탐색하는데 전에 visited값을 하나 증가시켜서 간다.
    if n2 in graph[n1]:
        print(cnt)
        exit()

    for i in graph[n1]:
        if i == n2:
            print(cnt)
            exit()
        if visited[i] == 0:
            dfs(graph ,i, n2)
    print(-1)
    exit(0)

# 촌수 계산
n = int(input())
n1 , n2 = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

for i in range(m):
    x , y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(graph, n1 , n2)



