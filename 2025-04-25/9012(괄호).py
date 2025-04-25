T = int(input())
arr = [ input() for i in range(T)]
a = '('
b = ')'
a_cnt = 0
b_cnt = 0
for i in range(T):
    c = arr[i]

    if len(c) % 2 != 0:
        print('NO')
        continue
    for j in range(len(c)):

        if c[j] == a:
            a_cnt += 1
        elif c[j] == b:
            b_cnt += 1

        if b_cnt > a_cnt:
            print('NO')
            break

    if b_cnt == a_cnt:
        print('YES')
    elif b_cnt < a_cnt:
        print('NO')
    a_cnt = 0
    b_cnt = 0