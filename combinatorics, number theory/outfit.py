import sys

n = int(sys.stdin.readline())

for i in range(n):
    rep = int(sys.stdin.readline())
    item_list = []
    num = 1
    cnt_dic = {}
    for j in range(rep):
        item1, item2 = sys.stdin.readline().split()
        item_list.append(item2)
    for key in item_list:
        if not key in cnt_dic:
            cnt_dic[key] = 1
        else:
            cnt_dic[key] += 1
    for key in cnt_dic:
        num *= cnt_dic[key] + 1
    result = num - 1
    print(result)
