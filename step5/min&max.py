#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())


num_list = list(map(int,input().split()))
min = num_list[0]
max = num_list[0]


for i in num_list:
    if i < min:
        min = i
    elif i > max:
        max = i

print(min, max)

#input
'''
5
20 10 35 30 7
'''
#output
'''
7 35
'''

