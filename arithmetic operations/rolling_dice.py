import sys
import collections

num_list = list(map(int, sys.stdin.readline().split()))

num_list2 = list(set(num_list))

if len(num_list2) == 3:
    print(max(num_list) * 100)
elif len(num_list2) == 1:
    print(10000 + num_list[0]*1000)
else:
    num = 0
    dic = collections.Counter(num_list)
    for key in dic.keys():
        if dic[key] == 2:
            num = key
    print(1000+(num * 100))






