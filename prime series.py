i=1
a=2
n=int(input("Enter the series value: "))
while(n!=0):
    for i in range(1,n):
        c=a%i
        if c==0:
            break
    else:
        print(a)
    a=a+1
    n=n-1
       

   
        
