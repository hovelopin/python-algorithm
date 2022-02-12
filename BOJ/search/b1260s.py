from collections import deque

graph = []

# DFS
def DFS(V):
    visited_DFS[V] =True
    print(V , end ='')
    for i in graph[V]:
        if not visited_DFS[i]:
            DFS()

# BFS
def BFS(V):
    queue = deque([V])
    visited_BFS[V] = True
    while queue:
        V = queue.popleft()
        print(V , end = '')
        for i in graph[V]:
            if not visited_BFS[i]:
                queue.append(i)
                visited_BFS[i] = True


N , M , V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort()

visited_DFS = [False] * (N+1)
visited_BFS = [False] * (N+1)

print(graph)