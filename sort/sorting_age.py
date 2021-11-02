import sys

n = int(input())
info_list = []

for i in range(n):
    age,name = sys.stdin.readline().split()
    info_list.append((age,name))

info_list.sort(key = lambda x: int(x[0]))

for info in info_list:
    print(info[0],info[1])
