import sys
sys.stdin=open("input.txt", "r")

n=int(input())
num=list()
for x in range(n):
  num.append(list(map(str,input().split())))
  num[x][1]=int(num[x][1])

num.sort(key=lambda x: x[1])

for j in range(n):
  print(num[j][0],end=" ")