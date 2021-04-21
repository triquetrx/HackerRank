def listtostr(s):
    str=""
    for ele in s:
        str+=ele
    return str
n=int(input())
flag=1
c=list(input())
for i in range(0,n-1):
    if c[i]=='H' and c[i+1]=='H':
        flag=0
        break
    if c[i]=='.':
        c.pop(i)
        c.insert(i,'B')
if c[n-1]=='.':
    c.pop(n-1)
    c.insert(n-1,'B')
if flag==1:
    print('YES')
    print(listtostr(c))
else:
    print('NO')
    
