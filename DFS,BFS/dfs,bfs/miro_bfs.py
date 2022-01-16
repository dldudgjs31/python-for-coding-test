## 예제
from collections import deque
import sys
sys.stdin=open("input.txt", "r")

## bfs
def bfs(x,y):
  queue=deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    ## 현재 위치에서 4가지 방향으로의 위치 확인
    for i in range(4):
      nx= x+ dx[i]
      ny= y+ dy[i]
      # 미로 공간 벗어난 여부 체크
      if nx < 0 or nx >= n or ny <0 or ny >= m:
        continue
      #벽인경우 무시(괴물)
      if graph[nx][ny]==0:
        continue
      # 처음방문하는 노드인경우 최단거리 기록하기
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
  ## 가장 오른쪽 최단 거리 반환
  return graph[n-1][m-1]

###두 정수 입력받기
n,m=map(int,input().split())

### 2차원 배열 받기
graph=[]
for _ in range(n):
  graph.append(list(map(int,input())))

## 상하좌우 정의
##for문으로 돌리기 위함
dx=[-1,1,0,0]
dy=[0,0,-1,1]

## bfs를 수행한 결과
print(bfs(0,0))
