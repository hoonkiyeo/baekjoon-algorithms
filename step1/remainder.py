#!/usr/bin/env python
# coding: utf-8

# In[1]:


A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#input
'''
5 8 4
'''
#ouput
'''
1
1
0
0
'''

