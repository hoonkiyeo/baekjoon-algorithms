import sys

num = int(sys.stdin.readline())


sum = 0
N = 0
for i in range(1, num+1):
    sum += i
    N += 1
    if sum > num:
        N -= 1
        break

print(N)