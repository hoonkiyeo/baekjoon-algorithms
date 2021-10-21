import sys
rep = int(input())
w_h_list = [] #weight and height information list

for i in range(rep):
    weight,height = map(int, sys.stdin.readline().split())
    w_h_list.append((weight,height))

for i in w_h_list:
    rank = 1
    for j in w_h_list:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]: #i[0] and j[0] = weight, i[1] and j[1] = height
                rank += 1
    print(rank)










