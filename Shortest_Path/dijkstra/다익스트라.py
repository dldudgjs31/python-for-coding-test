'''
노드 개수/간선개수
6 11
시작 노드 번호
1
간선 정보
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
import sys
sys.stdin=open("input.txt", "r")

# 무한을 의미하는 값으로 10억 설정
INF=int(1e9)

# 노드 개수 및 간선 개수 입력 받기
n,m=map(int,input().split())

# 시작 노드 번호 
start=int(input())

# 각노드 정보를 담는 리스트 생성
graph=[[] for i in range(n+1)]

# 노드별 최단거리 초기화(INF로 초기화)
distance=[INF]*(n+1)

#  방문한 적 있는지 체크 여부 리스트
visited=[False]*(n+1)

#모든 간선 정보 입력 받기
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

print(graph)

# 방문하지 않는 노드 중에서 가장 최단거리가 짧은 노드의 번호 반환하는 함수
def get_smallest_node():
  min_value=INF
  index=0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value= distance[i]
      index=i
  return index

def dijkstra(start):
  #시작노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작노드를 제외한 전체 n-1 개의 노드에 대해 반복
  for i in range(n-1):
    #현재 최단거리가 가장짧은 노드를 꺼내서 방문처리
    now=get_smallest_node()
    visited[now]=True

    # 현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])