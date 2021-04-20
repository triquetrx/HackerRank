n=int(input())
arr=list(map(int, input().strip().split()))
p=max(arr)
d=0
for i in range(len(arr)):
    if arr[i]!=p:
        d+=1
print(d)
