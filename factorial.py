def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

A = 3
print(fact(A))