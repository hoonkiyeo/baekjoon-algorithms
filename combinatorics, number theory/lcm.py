import sys

n = int(sys.stdin.readline())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    lcm = int(g * (a / g) * (b / g))
    print(lcm)



