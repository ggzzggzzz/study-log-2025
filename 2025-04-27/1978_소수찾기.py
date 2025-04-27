N = int(input())
cnt = 0
arr = list(map(int, input().split()) )

for k in range(len(arr)):
    if arr[k] == 1:
        continue
    flag = True
    for j in range(3,arr[k] ):


        if arr[k] % 2 == 0:
            flag = False
            break
        elif arr[k] % j == 0:
            flag = False
            break
    if flag:
        cnt += 1
    else:
        flag = True
print(cnt)