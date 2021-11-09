import sys

num_list = list(map(int, sys.stdin.readline().split()))
num_list = sorted(num_list)
result = num_list[1]

print(result)