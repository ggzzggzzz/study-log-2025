N = int(input())
arr = []
for i in range(1,N+1):
    a = int(input())
    arr.append(a)
arr.sort()
for i in range(N):
    print(arr[i])

