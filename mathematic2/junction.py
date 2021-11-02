import math
import sys

rep = int(input())

for _ in range(rep):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 > r2 + distance or r2 > r1 + distance or distance > r1+r2:
            print(0)
        elif r1 + r2 == distance or abs(r1-r2) == distance:
            print(1)
        else:
            print(2)
