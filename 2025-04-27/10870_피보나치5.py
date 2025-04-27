def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        b = fibo(a-1) + fibo(a-2)
        return b

n = int(input())
print(fibo(n))
#