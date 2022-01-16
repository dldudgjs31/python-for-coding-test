## DFS
## 깊이 우선 탐색
## 깊은 부분 우선적으로 탐색
## 스택 자료구조 및 재귀함수 이용
def dfs(graph,v,visited):

  # 현재 노드 방문처리
  visited[v]=True
  print(v,end=" ")
  # 현재노드와 연결된 노드 재귀적 방문 스타토
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited=[False]*9

dfs(graph,1,visited)