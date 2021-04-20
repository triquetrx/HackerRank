import math
nm = list(map(int,input().strip().split()))
n=nm[0]
m=nm[1]
a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))
lcm_num = a[0]
gcd_num = b[0]
if len(a) > 1:
    for x in range(1,len(a)):
        lcm_num =  (lcm_num * a[x])//math.gcd(lcm_num,a[x])
    if len(b) > 1:
        for x in range(1,len(b)):
            gcd_num = math.gcd(gcd_num,b[x])
    count = 0
    for x in range(lcm_num, gcd_num+1, lcm_num):
        if math.gcd(x, gcd_num) == x:
            count += 1
    print(count)
