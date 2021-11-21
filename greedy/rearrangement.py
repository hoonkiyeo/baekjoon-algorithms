import sys

n = int(sys.stdin.readline())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))


min_val = 0
for _ in range(n):
    min_val += min(a_list) * max(b_list)
    a_list.pop(a_list.index(min(a_list)))
    b_list.pop(b_list.index(max(b_list)))

print(min_val)
