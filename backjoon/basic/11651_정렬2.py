#5
#0 4
#1 2
#1 -1
#2 2
#3 3
n=int(input())
number=list()
for _ in range(n):
    number.append(list(map(int,input().split())))
number.sort(key=lambda x: (x[1],x[0]))
for y in range(n):
    print(number[y][0],number[y][1])
                  