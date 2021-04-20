a=['h','e','l','l','o']
c=len(a)
print(len(a))
print(a)
n=int(input("Enter the position to change"))
#print("sum of array is")
#sum=a[0]+a[c-1]
#print(sum)
for i in range(0,c):
    if(i==n):
        a.pop(n)
        b=str(input("Enter the value"))
        a.insert(n, b)
print(a)
