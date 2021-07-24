#!/usr/bin/env python
# coding: utf-8

# In[5]:


n,x = map(int,input().split())
num_list = list(map(int,input().split()))

for num in num_list:
    if num < x:
        print(num, end = ' ')
        
#input
'''
10 5
1 10 4 9 2 3 8 5 7 6
'''
#output
'''
1 4 2 3
'''

