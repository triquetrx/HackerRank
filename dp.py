l=int(input())
n=int(input())
for i in range(n):
    w=list(map(int, input().split()))
    w0=w[0]
    h0=w[1]
    if w0==l and h0==l:
        print("ACCEPTED")
    elif w0 or h0<l:
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")
