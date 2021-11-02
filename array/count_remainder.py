#!/usr/bin/env python
# coding: utf-8

# In[10]:


rm_list = []
for i in range(10):
    x = int(input())
    if (x % 42) in rm_list:
        continue
    else:
        rm_list.append(x % 42)
print(len(rm_list))


#input
'''
39
40
41
42
43
44
82
83
84
85
'''
#output
'''
6
'''

