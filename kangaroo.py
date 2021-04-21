a = list(map(int, input().rstrip().split()))
x1=a[0]
v1=a[1]
x2=a[2]
v2=a[3]
n=0
if v1>v2:
    for i in range(10000):
        x1=x1+v1
        x2=x2+v2
        if x1==x2:
            n=n+1
    if n>0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
