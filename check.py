import math
import os
import random
import re
import sys
p=0
m=0
n=0
a=int(input())
x = list(map(int,input().strip().split()))[:a] 
for i in range(0,a):
    if x[i]>0:
        p=p+1
    elif x[i]==0:
        n=n+1
    else:
        m=m+1
print(p/a)
print(m/a)
print(n/a)
