import sys

n = int(sys.stdin.readline())

for i in range(n):
    in_str = list(map(str, sys.stdin.readline()))
    cnt = 0
    for p in in_str:
        if p == "(":
            cnt += 1
        elif p == ")":
            cnt -= 1
        if cnt == -1:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
