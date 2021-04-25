kl=list(map(int, input().strip().split()))
k=kl[0]
l=kl[1]
count=0
s=0
a=list(map(int, input().strip().split()))[:k]
for i in range(len(a)):
    for j in range(len(a)):
        if i<j:
            s=a[i]+a[j]
            if s%l==0:
                count+=1
print(count)
