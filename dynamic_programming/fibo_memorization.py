'''
피보나치 수열 
-단순 재귀
-위에서 아래로 내려가는 방식
'''
''''
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1)+fibo(x-2)

print(fibo(4))
'''
'''
메모이제이션
'''
dp=[0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  #이미 계산한 문제라면 그대로 반환
  if dp[x]!=0:
    return dp[x]

  dp[x]=fibo(x-1)+fibo(x-2)
  return dp[x]
print(fibo(10))
print(dp[1::])