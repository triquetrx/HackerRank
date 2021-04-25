def lsttostrs(c):
    st=""
    for ele in c:
        st+=ele
    return st
s=str(input())
c=[]
for i in range(len(s)):
    it=0
    c.append(it)
for i in range(len(s)):
    if s[i].isupper():
        c.pop(i)
        c.insert(i,(s[i].lower()))
    else:
        c.pop(i)
        c.insert(i,(s[i].upper()))
print(lsttostrs(c))

