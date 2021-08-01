#!/usr/bin/env python
# coding: utf-8

# In[3]:


def odd_comparison(a, b):
    
    a = int(str(a)[::-1])
    b = int(str(b)[::-1])
    
    if a > b:
        return a
    else:
        return b
    
a,b = map(int,input().split())
result = odd_comparison(a, b)
print(result)

#input
'''
839 237
'''
#output
'''
938
'''

