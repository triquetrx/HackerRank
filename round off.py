a=[]
m=0
d=0
z=0
n=int(input())
for i in range(0,n):
    it=int(input())
    a.append(it)
for i in range(0,n):
    if a[i] >33:
        d=a[i]//5
        if a[i]%5==0:
            print(a[i])
        else:
            z=5*(d+1)
            if z-a[i]<3:
                print(z)
            else:
                print(a[i])
    else:
        print(a[i])
