# DFS/BFS (이코테)

많은 양의 데이터중에서 원하는 데이터를 찾는 과정

스택 자료구조

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- 입구와 출구가 동일한 형태로 스택을 시각화

파이썬에서의 구현

```python
stack=[]
stack.append()
stack.pop()
print(stack[::-1])#최상단 원소부터 출력
print(stack) #최하단 원소부터 출력
```

![Untitled](DFS%20BFS%20(%E1%84%8B%E1%85%B5%E1%84%8F%E1%85%A9%E1%84%90%E1%85%A6)%201077dcafd9c24ede8206f74f15182aec/Untitled%201.png)

큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 선입선출 자료구조
- 큐는 입구 출구가 모두 뚫려있는 터널같은 형태로 시각화

```python
from collections import deque
queue=deque()
queue.append(6)
queue.append(5)
queue.pop(left)

print(queue) #들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력

```

재귀함수

- 재귀함수를 문제 풀이에서 사용할때는 재귀 함수의 종료 조건을 반드시 명시해야함
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
- 종료 조건을 포함한 재귀 함수 예제

```python
def recursive_function(i):
	#100번 호출시 종료되도록 종료 조건 명시
	# 시작부분에 명시
	if i==100:
		return
	print(i, '번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
	recursive_function(i+1)
	print(i,'번째 재귀함수를 종료합니다.')
recursive_function(1)
```

ex)

팩토리얼 구현 예제

```python
def factorial_iterative(n):
	result=1
	for i in range(1,n+1):
		result*=i
	return result
def factorial_recursive(n):
	if n<=1: # n이 1이하인 경우 1을 반환
		return 1
	return n*factorial_recursive(n-1)

print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_recursive(5))
```

 ex)

최대공약수 계산 (유클리드 호제법) 예제

- 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘중 하나
- 유클리드 호제법
    - 두 자연수 a,b에 대하여 (a>b) a를 b로 나눈 나머지를 R이라고 합시다
    - 이때 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같다.
    - 유클리드 호제법의 아이디어를 구대로 재귀함수로 작성 가능
    
    | 단계 | A | B |
    | --- | --- | --- |
    | 1 | 192 | 162 |
    | 2 | 162 | 30 |
    | 3 | 30 | 12 |
    | 4 | 12 | 6 |
    
    ```python
    def gcd(a,b):
    	if a%b==0:
    		return b
    	else:
    		return gcd(b,a%b)
    print(gcd(192,162))
    ```
    

DFS

- 깊이 우선 탐색이라고 하며, 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조를 사용하며 구체적인 동작 과정은 다음과 같다
    - 탐색 시작 노드를 스택에 삽입하고 방문처리
    - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리, 방문하지 않은 인접 노드가없으면 스택에서 최상단 노드를 꺼냄
    - 더 이상 2번의 과정을 수행할 수 없을때까지 반복한다.
    
    ![Untitled](DFS%20BFS%20(%E1%84%8B%E1%85%B5%E1%84%8F%E1%85%A9%E1%84%90%E1%85%A6)%201077dcafd9c24ede8206f74f15182aec/Untitled%202.png)
    
    1 → 2 → 7 → 6 → 8 → 3 → 4 → 5
    
    ```python
    # DFS 메서드 정의
    def dfs(graph,v,visited):
    	#현재 노드를 방문처리
    	visited[v]=True
    	print(v,end=' ')
    	#현재 노드와 연결된 다른 노드를 재귀적으로 방문
    	for i in graph[v]:
    		if not visited[i]:
    			dfs(graph,i,visited)
    
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
    
    #각 노드가 방문된 정보를 표현 (1차원 리스트)
    visited=[False]*9
    
    #정의된 dfs 함수 호출
    dfs(graph,1,visited)
    
    #결과
    #1 2 7 6 8 3 4 5
    ```
    

BFS

- 너비우선탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐자료구조를 이용함
    1. 탐색 시작 노드를 큐에 삽입하고 방문처리
    2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접노드중에서 방문하지 않을 노드를 모두큐에 삽입하고 방문처리
    3. 더이상 2번의 과정을 수행할 수 없을때까지 반복
        
        ![Untitled](DFS%20BFS%20(%E1%84%8B%E1%85%B5%E1%84%8F%E1%85%A9%E1%84%90%E1%85%A6)%201077dcafd9c24ede8206f74f15182aec/Untitled%203.png)
        
    
    1-2-3-8-7-4-5-6
    
    ```python
    from collections import deque
    
    #BFS 메서드 정의
    def bfs(graph,start,visited):
    	#큐 구현을 위해 deque 라이브러리 사용
    	queue=deque([start])
    	# 현재 노드를 방문처리
    	visited[start]=True
    	#큐가 빌때까지 반복
    	while queue:
    		#큐에서 하나의 원소를 뽑아 출력하기
    		v=deque.popleft()
    		print(v,end=' ')
    		#아직 방문하지 않은 인접한 원소들을 큐에 삽입
    		for i in graph[v]:
    			if not visited[i]:
    				queue.append(i)
    					visited[i]=True
    
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
    #각 노드가 방문된 정보를 표현
    visited=[False]*9
    # 정의된 bfs 함수 호출
    bfs(graph,1,visited)		
    ```