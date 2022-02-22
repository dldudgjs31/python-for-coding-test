#3
#21 Junkyu
#21 Dohyun
#20 Sunyoung

n=int(input())
signup=[[0]*2 for i in range(n)]
for x in range(n):
    age,name=map(str,input().split())
    signup[x][0]=int(age)
    signup[x][1]=name
signup.sort(key=lambda x: x[0])
for y in range(n):
    print(signup[y][0],signup[y][1])