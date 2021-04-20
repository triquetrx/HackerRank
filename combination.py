from itertools import combinations
c=0
z=0
a=[]
k=(range(1,int(input())+1))
s=input().split()
n=int(input())
for i in range(len(s)):
    if s[i]=='a': 
        a.append(i+1)
for i in combinations(s,n):
    c+=1
    z+= 'a' in i
print(z)
print(c)
#print(float(z/c))
