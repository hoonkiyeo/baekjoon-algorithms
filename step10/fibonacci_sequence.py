#Fn = F(n-1) + F(n-2) (n>=2)

n = int(input()) # n<=20


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(fib(n))



