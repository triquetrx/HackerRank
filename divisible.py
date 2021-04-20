def convert(list):  
    s = [str(i) for i in list] 
    res = int("".join(s)) 
    return(res)
n=int(input())
a=list(map(int, input().strip().split()))[:n]
b=[]
c=[]
d=[]
for i in range(n//2):
    it=a[i]
    b.append(it)
    t=a[n-1-i]
    c.append(t)
c.reverse()
for i in range(len(b)):
    count = 0
    n=b[i]
    while n != 0: 
        n //= 10
        count+= 1
    it=b[i]//(10**(count-1))
    d.append(it)
for i in range(len(c)):
    count = 0
    n=c[i]
    while n != 0: 
        n //= 10
        count+= 1
    it=c[i]%(10**(count-1))
    d.append(it)
e=convert(d)
if e%11==0:
    print("OUI")
else:
    print("NON")
