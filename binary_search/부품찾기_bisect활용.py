'''
부품찾기
5
8 3 7 9 2
3
5 7 9
'''
import sys
from bisect import bisect_left, bisect_right
sys.stdin=open("input.txt", "r")

n=int(input())
products=list(map(int,input().split()))
m=int(input())
find=list(map(int,input().split()))

#5개의 부품 sort
products.sort()

#찾는 부품 존재여부 판별
#bisect 라이브러리 사용하여 left/right 값이 같다면 존재하지 않는 걸로 판별하여 no
for x in range(m):
  if bisect_left(products,find[x])==bisect_right(products,find[x]):
    print("no",end=" ")
  else:
    print("yes", end=" ")
