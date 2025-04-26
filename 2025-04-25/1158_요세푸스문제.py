N, k = map(int, input().split())
arr = [i + 1 for i in range(N)]
result = []
a = 0

for i in range(N):
    a = (a + k - 1) % len(arr)
    result.append(arr.pop(a))

print("<" + ", ".join(map(str, result)) + ">")
