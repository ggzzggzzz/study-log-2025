def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1,cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1,cnt)

def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt)
T = int(input())
s = list(input() for i in range(T))

for i in range(len(s)):
    a , b = isPalindrome(s[i])
    print(a,b)


