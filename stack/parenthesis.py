import sys

n = int(input())

for i in range(n):
    vps = sys.stdin.readline()
    cnt = 0
    for p in vps:
        if p == "(":
            cnt += 1
        if p == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")