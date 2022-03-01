computer = int(input())
pair = int(input())

graph = [[] for _ in range(computer+1)]

# 컴퓨터를 모두 연결해준다.
for i in range(pair):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (computer+1)
cnt = 0

def dfs(n):
    global cnt
    visited[n] = 1
    cnt+=1
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)
    return cnt

dfs(1)
print(cnt-1)