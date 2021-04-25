import math
a=int(input())
y=0
x = list(map(int,input().strip().split()))[:a] 
for i in range(0,a):
    y=y+x[i]
print(y)
