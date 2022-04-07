tc = int(input())
n = int(input())
m = int(input())

graph=[[] for _ in range(n+1)]
for j in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
print(len(graph[4]))