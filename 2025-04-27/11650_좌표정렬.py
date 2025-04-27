N = int(input())
arr = []
for i in range(1, N+1):
    a,b = map(int,input().split()) 

    arr.append((a,b))

arr.sort()

for a, b in arr:
    print(a,b)
