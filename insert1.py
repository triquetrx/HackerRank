def insertionSort1(n, arr):
    n-=1
    i = arr[n]
    while n>0:
        if i > arr[n-1]:
            arr[n] = i
            print(arr)
            break
        else:
            arr[n] =arr[n-1]
            print(arr)
        n-=1
    else:
        arr[0] = i
        print(arr)
n = int(input())
arr = list(map(int,input().split()))
