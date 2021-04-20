st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
og=0
ap=0
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
z=[]
x=[]
for i in range(len(apples)):
    it=0
    z.append(it)
for i in range(len(oranges)):
    it=0
    x.append(it)
print(len(apples))
for i in range(0,len(apples)):
    z[i]=a+apples[i]
for i in range(0,len(oranges)):
    x[i]=b+oranges[i]
for i in range(len(z)):
    if s<=z[i]<=t:
        ap=ap+1
print(ap)
for i in range(len(x)):
    if s<=x[i]<=t:
        og=og+1
print(og)
                
