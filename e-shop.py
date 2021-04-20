n, k=list(map(int, input().split()))
h=list(map(int, input().strip().split()))
p=max(h)
if p<h:
    print('0')
else:
    print(p-h)
