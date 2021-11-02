
import sys
n = int(input())
info_list = []

for i in range(n):
    w,h = map(int, sys.stdin.readline().split()) #weight and height
    info_list.append((w,h)) #append weight and height of each person

for info in info_list:
    rank = 1
    for info2 in info_list:
        #comparing info and info2
        if info[0] != info2[0] and info[1] != info2[1]:
            if info[0] < info2[0] and info[1] < info2[1]:
                rank += 1
    print(rank)









