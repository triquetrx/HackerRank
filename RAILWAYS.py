t=int(input())
m=0
for i in range(0,t):
    N=int(input())
    m=N%12
    if m==1:
        print(N+11,"WS")
    elif m==0:
        print(N-11,"WS")
    elif m==2:
        print(N+9,"MS")
    elif m==3:
        print(N+7,"AS")
    elif m==4:
        print(str(N+5)+'AS')
    elif m==5:
        print(N+3,"MS")
    elif m==6:
        print(N+1,"WS")
    elif m==7:
        print(N-1,"WS")
    elif m==8:
        print(N-3,"MS")
    elif m==9:
        print(N-5,"AS")
    elif m==10:
        print(N-7,"AS")
    else:
        print(N-9, "MS")
