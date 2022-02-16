'''
5
3 4
1 1
1 -1
2 2
3 3
'''
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
target1=[0]*n
for x in range(n):
  target1[x]=list(map(int,input().split()))

target1.sort(key=lambda x: (x[0],x[1]))

for y in range(n):
    print(target1[y][0],target1[y][1])