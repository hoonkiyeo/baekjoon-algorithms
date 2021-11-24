import sys

n = int(sys.stdin.readline())

sum = 0
for i in range(n):
    sum = 0
    in_str = sys.stdin.readline().split(",")
    sum += int(in_str[0]) + int(in_str[1])
    print(sum)