a=list(map(int, input().split()))[:3]
b=list(map(int, input().split()))[:3]
al=0
bo=0
for i in range(0,3):
    if a[i]>b[i]:
        al=al+1
    elif a[i]<b[i]:
        bo=bo+1
    else:
        al=al+0
        bo=bo+0

print(al,bo)
