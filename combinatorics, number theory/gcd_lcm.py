import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    g = gcd(a,b)
    return int(g * (a/g) * (b/g))

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    print(gcd(a,b))
    print(lcm(a,b))