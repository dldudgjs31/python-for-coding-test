import sys
sys.stdin=open("input.txt", "r")

n,k=map(int,input().split())
num=[0]*2
for x in range(2):
  num[x]=list(map(int,input().split()))

##1.첫번째 줄의 숫자의 합의 최대값 만들기
##2.첫번째 줄의 최소값과 두번째줄의 최대값 교환방식 
##3. 첫번째 줄 sort
##4. 두번째 줄 sort 역순
##5. K 번째까지 교환
num[0].sort()
num[1].sort(reverse=True)
for i in range(k):
  num[0][i],num[1][i]=num[1][i],num[0][i]
print(sum(num[0]))