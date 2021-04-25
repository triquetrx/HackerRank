def merch(n,a):
    a.sort()
    c=0
    i=0
    while i<n-1:
        if a[i]==a[i+1]:
            c+=1
            i+=2
        else:
            i+=1
    return c

n=int(input())
a=list(map(int, input().strip().split()))[:n]
result=merch(n,a)
print(result)

