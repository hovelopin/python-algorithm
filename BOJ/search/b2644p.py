'''
내가 해결하려는 방향!
=> 루트부터 시작해서 7까지 가고 루트부터 시작해서 3까지 가는 방법으로 해결하려고 했다!

대부분의 사람들은 양방향으로 왔다갔다 할 수 있게 풀었음 ,,
'''

cnt = 0

N = int(input())

# 계산해야하는 관계
result1 , result2 = map(int,input().split())

M = int(input())
# x가 부모 y가 자식

graph = [[] for i in range(result1+1)]

for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)

def dfs(v,end):
    global cnt
    visited[v] = True
    cnt+=1
    for i in graph[v]:
        if i == end:
            break
        else:
            if not visited[i]:
                dfs(i,end)
    return True

visited = [False] * (N+1)
dfs(1,result1)
visited = [False] * (N+1)
dfs(1,result2)
print(cnt)



'''
[
    [],  0
    [2, 3],   1 
    [7, 8, 9],   2
    [],  3 
    [5, 6],   4
    [], 5 
    [],  6
    []   7 
]
'''