import sys
sys.stdin=open("input.txt", "r")

n=int(input())
num=list()
for x in range(n):
  num.append(int(input()))

num.sort(reverse=True)

for j in num:
  print(j,end=" ")