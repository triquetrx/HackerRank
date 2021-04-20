l, r, k=list(map(int, input().split()))
c=0
print(l)
print(k)
print(r)
for i in range(l,r+1):
    if i%k==0:
        c+=1
print(c)
