s=str(input())
cz=0
co=0
for i in range(len(s)):
    if s[i]=='z' or s[i]=='Z':
        cz+=1
    else:
        co+=1
if co==2*cz:
    print("Yes")
else:
    print("No")
