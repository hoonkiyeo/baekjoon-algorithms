import sys
import math

n = int(sys.stdin.readline())
num = math.factorial(n)

cnt = 0
for i in str(num)[::-1]:
    if i == '0':
        cnt += 1
    if i != '0':
        break

print(cnt)


