import sys
sys.stdin=open("input.txt", "r")

#DFS로 특정 노드를 방문하고 연결된 모든 노드 방문
def dfs(x,y):
  # 주어진 범위를 벗어나는 경우 즉시 종료
  if x <= -1 or x >= dept or y<=-1 or y >= breadth:
    return False

  # 현재 노드 방문 처리
  if ice[x][y]==0:
    #해당 노드 방문 처리
    ice[x][y]=1
    #상하좌우 재귀 호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

dept,breadth=map(int,input().split())
ice=[]

for i in range(dept):
  ice.append(list(map(int,input())))

result=0
for i in range(dept):
  for j in range(breadth):
    if dfs(i,j)==True:
      result+=1
print(result)

