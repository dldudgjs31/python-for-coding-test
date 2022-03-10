'''
입력
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다. 

출력
잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.

()(((()())(())()))(())
17
'''
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n=list(sys.stdin.readline())
stack=deque()
sum=0
for x in range(len(n)):
  if n[x]=="(":
    stack.append(n[x])
  elif n[x]==")" and n[x-1]=="(":
    stack.pop()
    sum+=len(stack)
  elif n[x]==")" and n[x-1]==")":
    stack.pop()
    sum+=1

print(sum)