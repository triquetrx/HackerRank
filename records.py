n=int(input())
a=list(map(int, input().strip().split()))[:n]
m=0
x=0
high=[]
for i in range(0,n):
    it=0
    high.append(it)
    high[0]=a[0]
low=[]
for i in range(0,n):
    it=0
    low.append(it)
    low[0]=a[0]
for i in range(1,len(a)):
    if high[i-1]<a[i]:
        high[i]=a[i]
        m+=1
    else:
        high[i]=high[i-1]
for i in range(1,len(a)):
    if low[i-1]>a[i]:
        low[i]=a[i]
        x+=1
    else:
        low[i]=low[i-1]
print(high)
print(low)
print(m,x)

            
