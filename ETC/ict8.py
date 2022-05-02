# 21시 50분 ( 시작 ) =>  22시 16분 ( 끝 ) =====>  26분
# 특정 거리의 도시 찾기 ( DFS & BFS )

from collections import deque
import sys

n , m , k , x = map(int,sys.stdin.readline().split())

# nList는 도로 checkCnt는 방문횟수를 기록하기 위해 result는 checkCnt에서 k번째랑 횟수가 같은 것을 골라서 담은 것
nList = [[] for _ in range(n+1)]
checkCnt = [0] * (n+1)
result = []

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    # queue가 빌때까지 반복해서 돈다.
    while queue:
        v = queue.popleft()
        for i in nList[v]:
            if not visited[i]:
                checkCnt[i] = checkCnt[v] + 1
                queue.append(i)
                visited[i] = True

for i in range(m):
    a , b =map(int,sys.stdin.readline().split())
    nList[a].append(b)

# 방문했는지 알아보기 위해서 도시의 갯수 + 1 만큼
visited = [False] * (n+1)
bfs(x)

# k랑 맞는 index를 넣기 위해서
idx = 0
for i in checkCnt:
    if(i == k):
        result.append(idx)
    idx += 1

# 하나도 존재하지 않으면 -1 존재하면 도시번호를 한줄에 하나씩 오름차순으로 출력
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)

"""
테스트 케이스 1
4 4 2 1
1 2
1 3 
2 3
2 4
"""