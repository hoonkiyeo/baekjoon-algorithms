

#h = story of the hotel
#w = number of rooms on each floor
#n = Nth guest

rep = int(input())
for i in range(rep):
    h,w,n = map(int,input().split())
    if n % h != 0:
        floor = n % h
        num = (n//h) + 1
    else:
        floor = h
        num = n // h

    assigned_room = floor * 100 + num
    print(assigned_room)


#input
'''
2
6 12 10
30 50 72
'''
#output
'''
402
1203
'''







