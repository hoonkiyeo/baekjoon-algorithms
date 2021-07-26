#!/usr/bin/env python
# coding: utf-8

# In[5]:


while True:
    try:
        x,y = map(int,input().split())
        print(x+y)
    except:
        break
        
#input
'''
1 1
2 3
3 4
9 8
5 2
12
'''
#output
'''
2
5
7
17
7
12
'''

