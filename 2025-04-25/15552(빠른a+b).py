import sys
T = int(sys.stdin.readline())
c = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    c.append(a + b)

for i in c:
    print(i)