import array
n=int(input("Enter the series value: "))
def prime(x):
    i=1
    a=2
    t=0
    for i in range(1,x):
        for j in range(2,int((i+1)/2)):
            c=a%j
            if c==0:
                break
        else:
            return(a)
        x=x+1
def fibo(y):
    a=0
    b=1
    #print("\n",b)
    for i in range(1, y):
        c=a+b
        a=b
        b=c
        print("\n",a)
        i=i-1
if n%2==0:
    fibo(n)
else:
    prime(n)
