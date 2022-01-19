'''
떡볶이 떡 만들기
떡의 개수 4
떡의 길이 6
4 6
19 15 10 17
'''
'''
1. 떡의 중간값 mid 지정 후
2. 1step 진행 하여 떡 값에 -mid 값 총합이 m보다 작으면 end가 mid-1 크면 start가 mid+1 변경
3. 길이값이 동일하면 해당 값을 반환
'''
import sys

def cutting_rice(ricecake,target,start,end):
  while start<=end:
    mid = (start+end)//2 
    temp=0

    # mid값 뺀 떡의 길이 구하기
    for cake in ricecake:
      if mid < cake:
        temp+=(cake - mid)
    # 길이가 같으면 리턴 아니면 다시
    if temp == target:
      return mid
    elif temp > target:
      start=mid+1
    else:
      end=mid-1



sys.stdin=open("input.txt", "r")

n,m=map(int,input().split())
ricecake=list(map(int,input().split()))
ricecake.sort()
result=cutting_rice(ricecake,m,ricecake[0],ricecake[n-1])
print(result)
