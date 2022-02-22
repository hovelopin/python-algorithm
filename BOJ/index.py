# 연습장

# dfs
def dfs(graph , v , visited):
  visited[v] = True
  print(v , end =' ')
  # 인접 노드 방문
  for i in graph[v]:
    # 만일 아직 방문하지 않았다면
    if not visited[i]:
      dfs(graph , i , visited)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
