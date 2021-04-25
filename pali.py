def isPalindrome(s):
    a=0
    rev = ''.join(reversed(s))
    if (s == rev):
        a=1
    return a
s = str(input())
ans = isPalindrome(s)
if ans==1:
    print('YES')
else:
    print('NO')
