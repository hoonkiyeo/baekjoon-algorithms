#!/usr/bin/env python
# coding: utf-8

# In[6]:


num_list = []
for i in range(9):
    x = int(input())
    num_list.append(x)

max = num_list[0]

for i in num_list:
    if i > max:
        max = i
        
for i in range(len(num_list)):
    if num_list[i] == max:
        index = i + 1
        
print(max)
print(index)

#input
'''
3
29
38
12
57
74
40
85
61
'''
#output
'''
85
8
'''

