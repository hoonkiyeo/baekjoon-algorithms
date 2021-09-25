m, n = map(int, input().split())

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(m, n+1):
    if is_prime(i):
        print(i)

#input
'''
3 11
'''
#output
'''
3
5
7
11
'''