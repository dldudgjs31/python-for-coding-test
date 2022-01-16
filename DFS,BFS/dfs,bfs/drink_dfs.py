## 예제
## 음료수 얼려먹기
## DFS 사용
import sys
sys.stdin=open("input.txt", "r")
##노드 방문하는 DFS 코딩

def dfs(x,y):
  ## 검증
  ## 범위 벗어나는 값들은 처내기
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
 
  #해당 노드 방문여부 체크 방문이면 1로 변경
  if graph[x][y]==0: 
    graph[x][y]=1
    # 현재 x y 기준으로 상하좌우 방향으로 검증
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    # 해당 로직이 끝나면 true 반환으로 result값 증가시키기
    return True
  return False

## 입력값 받기
##가로 세로 길이 받기 nm
n,m=map(int,input().split())
## 2차원리스트 받기
graph=[]
for _ in range(n):
  graph.append(list(map(int,input())))

## 모든 노드 음료수 채우기
result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1

print(result)