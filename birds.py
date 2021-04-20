l=int(input())
a=list(map(int, input().strip().split()))
count=0
z=[]
z=[0,0,0,0,0,0]
for i in range(len(a)):
    z[a[i]] += 1
print(z)
print(z.index(1))
