import math
import sys

rep = int(input())

for _ in range(rep):
    x,y = map(int,sys.stdin.readline().split())
    distance = y - x
    cnt = 0

    num = math.floor(math.sqrt(distance))
    num_square = num ** 2
    increase_num = math.sqrt(num_square)

    if distance > num_square + increase_num:
        cnt = 2 * num + 1
    elif distance > num_square and distance <= num_square + increase_num:
        cnt = 2 * num
    elif distance == num_square:
        cnt = 2 * num - 1

    if distance < 4:
        cnt= distance

    print(cnt)


#input
'''
3
0 3
1 5
45 50
'''

#output
'''
3
3
4
'''
