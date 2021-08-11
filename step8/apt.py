
import sys

rep = int(input())

for _ in range(rep):
    floor = int(sys.stdin.readline()) #floor
    num = int(sys.stdin.readline()) #room_number
    resident = [i for i in range(1,num+1)] #first floor
    if floor == 0:
        print(resident[-1])
    for k in range(floor):
        for i in range(1,num):
            resident[i] += resident[i-1]
    print(resident[-1])
#input
'''
2
1
3
2
3
'''
#output
'''
6
10
'''








