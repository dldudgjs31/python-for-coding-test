
## BFS
## 너비우선 탐색
## 가까운 노드부터 우선적으로 탐색하는 알고리즘
## 큐자료 구조를 이용
## 
from collections import deque

def bfs(graph,start,visited):
  queue=deque([start])
  visited[start]=True

  #큐가 빌때까지 반복
  while queue: 
    v=queue.popleft()
    print(v, end=" ")

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True


# 각 노드가 연결된 정보 표현
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

# 각 노드가 방문된 정보 표현
# 노드 개수만큼 생성 인덱스때문에 +1 생성
visited=[False]*9
bfs(graph,1,visited)

