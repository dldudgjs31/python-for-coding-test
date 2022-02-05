'''
개미전사
N=창고 개수
1315 => 식량 개수
양옆 인근 창고는 불가
최대 획득량 측정

1113445
'''
import sys
sys.stdin=open("input.txt", "r")

n=int(input())
storage=list(map(int,input().split()))
total=0
for x in range(1,len(storage)):
  #좌우 값 비교
  if x==(n-1) and storage[x]>storage[x-1]:
    total+=storage[x]
  elif storage[x] > storage[x-1] and storage[x] >storage[x+1]:
    total+=storage[x]

print(total)