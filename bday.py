n=int(input())
a=list(map(int,input().strip().split()))[:n]
dm=list(map(int,input().strip().split()))
d=dm[0]
m=dm[1]
x=0
y=0
z=0
for i in range(n):
    while(z<m):
        x+=a[i+z]
        z+=1
    if x==d:
        y+=1
        print(y)
    if i+z==n:
        break
print(y)
