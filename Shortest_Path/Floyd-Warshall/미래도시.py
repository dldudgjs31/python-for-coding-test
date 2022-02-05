'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5         
'''
import sys
sys.stdin=open("input.txt", "r")

# 무한을 의미하는 값으로 10억 설정
INF=int(1e9)

# 회사 개수 및 경로 개수 입력 받기
n,m=map(int,input().split())

#2차원 리스트(그래프 표현)을 만들고 모든 값을 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n + 1):
  for b in range(1,n + 1):
    if a == b:
      graph[a][b] = 0


# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
# 서로 오갈수잇으므로 양방향 1 초기화
for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1


# 가야할 회사 x , 소개팅 들릴 k
x,k=map(int,input().split())


#점화식에 따라 플로이드 워셜 알고리즘 수행
#k 거처가는 노드
for k in range(1,n+1):
  #a 출발 노드
  for a in range(1,n+1):
    # b 도착 노드
    for b in range(1,n+1):
     graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

result=graph[1][k] + graph[k][x]

if result>=INF:
  print('-1')
else:
  print(result)
