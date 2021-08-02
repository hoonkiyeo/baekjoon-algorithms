#!/usr/bin/env python
# coding: utf-8

# In[32]:


def count_croatian(word):
    croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    cnt = 0
    
    for i in croatian:
        word = word.replace(i, "0")
        
    cnt += len(word)
    
    return cnt

word = input()
result = count_croatian(word)
print(result)

#input
'''
ddz=z=
'''
#output
'''
3
'''

