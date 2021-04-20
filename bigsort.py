n = int(input())
i=0
j=0
temp=0
un = []
for _ in range(n):
    unsorted_item = input()
    un.append(unsorted_item)
un.sort()
un.sort()
i=0
while i<n:
    print(un[i])
    i+=1
