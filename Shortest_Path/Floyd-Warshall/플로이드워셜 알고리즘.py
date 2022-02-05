#플로이드 워셜 알고리즘
'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
import sys
sys.stdin=open("input.txt", "r")
# 무한을 의미하는 값으로 10억 설정
INF=int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n=int(input())
m=int(input())

#2차원 리스트(그래프 표현)을 만들고 모든 값을 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n + 1):
  for b in range(1,n + 1):
    if a == b:
      graph[a][b] = 0
print(graph)

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
  # a에서 b로 가는 비용은 C라고 설정
  a,b,c=map(int,input().split())
  graph[a][b] = c
print(graph)

#점화식에 따라 플로이드 워셜 알고리즘 수행
#k 거처가는 노드
for k in range(1,n+1):
  # a 시작 노드
  for a in range(1,n+1):
    # b 도착 노드
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("Infinity",end=" ")
    else:
      print(graph[a][b], end=" ")
  print()



