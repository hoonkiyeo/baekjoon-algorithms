import sys

rep = int(input())

for _ in range(rep):
    floor = int(sys.stdin.readline()) #floor
    num = int(sys.stdin.readline()) #room_number
    resident_list = [i for i in range(1,num+1)] #first floor
    if floor == 0: #zero floor
        print(resident_list[-1])
    for k in range(floor):
        for i in range(1,num):
            resident_list[i] += resident_list[i-1]
    print(resident_list[-1])


#input
'''
2
1 first floor  
3 room number 3
2 second floor
3 room number 3
'''
#output
'''
6 residents in room number 3 on floor 1
10 residents in room number 3 on floor 2
'''








