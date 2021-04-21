def fact(n):
    if n!=1:
        return fact(n)*fact(n-1)
    else:
        return 1
n=int(input())
r=fact(n)
print(r)
