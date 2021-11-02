import sys

x_coor = []
y_coor = []

for _ in range(3):
    x,y = map(int, sys.stdin.readline().split())
    x_coor.append(x)
    y_coor.append(y)


for i in range(len(x_coor)):
    if x_coor.count(x_coor[i]) == 1:
        x = x_coor[i]
    if y_coor.count(y_coor[i]) == 1:
        y = y_coor[i]

print(x,y, sep=" ")

#input
'''
5 5
5 7
7 5
'''
#output
'''
7 7
'''