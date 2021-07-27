#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sys

n = int(input())
for _ in range(n):
    stu_list = list(map(int,sys.stdin.readline().split()))
    sum = 0
    avg = 0
    above_avg = []
    for i in range(1,len(stu_list)):
        sum += stu_list[i]
        avg = sum / stu_list[0]
        
    for i in range(1, len(stu_list)):
        if stu_list[i] > avg:
            above_avg.append(stu_list[i])
    
    percentage = (len(above_avg) / stu_list[0]) * 100
    print(format(percentage, ".3f") + "%")

#input
'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''
#output
'''
40.000%
57.143%
33.333%
66.667%
55.556%
'''

