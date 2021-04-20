from datetime import date
d1M1Y1 = input().split()
d1 = int(d1M1Y1[0])
m1 = int(d1M1Y1[1])
y1 = int(d1M1Y1[2])
d2M2Y2 = input().split()
d2 = int(d2M2Y2[0])
m2 = int(d2M2Y2[1])
y2 = int(d2M2Y2[2])
f_date = date(y1, m1, d1)
l_date = date(y2, m2, d2)

if l_date>f_date:
    print(0)
else:
    delta = f_date - l_date
    if m1>m2 and y1==y2:
        print((m1-m2)*500)
    else:
        print((delta.days)*15)
