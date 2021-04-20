kn=list(map(int, input().strip().split()))
k=kn[0]
n=kn[1]
no=0
op=0
a=list(map(int, input().strip().split()))[:k]
b=int(input())
sum=0
for i in range(k):
    sum=sum+a[i]
sum=sum-a[n]
no=sum/2
if no==b:
    print("Bon Appetit")
else:
    print(int(b-(sum/2)))
