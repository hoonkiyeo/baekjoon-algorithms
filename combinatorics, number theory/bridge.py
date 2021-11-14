import sys
import math

n = int(sys.stdin.readline())

def binom_coeff(n,k):
    coeff = math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
    return coeff

for i in range(n):
    w,s = map(int,sys.stdin.readline().split())
    if w == s:
        print(1)
    else:
        print(binom_coeff(s,w))





