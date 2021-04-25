def isConvertible(str1, str2, k): 
    if ((len(str1) + len(str2)) < k): 
        return True
    commonLength = 0
    for i in range(0, min(len(str1),len(str2)), 1): 
        if (str1[i] == str2[i]): 
            commonLength += 1
        else: 
            break 
    if ((k - len(str1) - len(str2) + 2 * commonLength) % 2 == 0): 
        return True
    return False

if __name__ == '__main__': 
    s=str(input())
    t=str(input())
    k=int(input())
    if (isConvertible(s, t, k)): 
        print("Yes") 
    else: 
        print("No") 
