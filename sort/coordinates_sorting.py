import sys

n = int(sys.stdin.readline())
coord_list = []

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    coord_list.append((x,y))

coord_list.sort(key = lambda x: (x[0], x[1]))
for coord in coord_list:
    print(coord[0], coord[1])