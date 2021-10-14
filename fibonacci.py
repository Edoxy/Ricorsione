
def fib(a, b, i, end):
    if (i == end):
        return a
    else:
        t = b
        b = a + b
        a = t
        i += 1
        result = fib(a, b, i, end)
    return result


def fib1(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    f = fib1(n-1) + fib1(n-2)
    return f


A = 2
print(fib(0, 1, 1, A))

