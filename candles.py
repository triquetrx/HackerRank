n=int(input())
a = list(map(int, input().rstrip().split()))[:n]
m=max(a)
c=0
for i in range(n):
    if(a[i]==m):
        c+=1
print(c)

