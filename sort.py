import time
a=[]
n=int(input("Enter The number elements to be: "))
for i in range(0,n):
   ip=int(input())
   a.append(ip)
print(a)
print(len(a))
print("*******Sorting*******")
time.sleep(n)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print("Soted data")
for i in range(0,n):
    print(a[i])
