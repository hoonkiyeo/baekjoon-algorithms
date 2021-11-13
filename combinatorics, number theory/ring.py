import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
denom = 0
numer = 0

start = num_list[0]

for i in range(1, len(num_list)):
    denom = start // gcd(start, num_list[i])
    numer = num_list[i] // gcd(start, num_list[i])
    print(denom, "/", numer, sep="")


