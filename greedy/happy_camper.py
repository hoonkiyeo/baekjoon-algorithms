import sys
cnt = 0

while True:
    ans = 0
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0 and p == 0 and v == 0:
        break
    else:
        cnt += 1
        ans += (l * (v // p)) + min(v % p, l)
        print("Case ", cnt, ": ", ans, sep = "")
