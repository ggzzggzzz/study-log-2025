def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


T = int(input())
lcm = []
for i in range(T):

    a,b = map(int, input().split())
    lcm.append( (a*b) // gcd(a, b))

for i in range(T):
    print(lcm[i])