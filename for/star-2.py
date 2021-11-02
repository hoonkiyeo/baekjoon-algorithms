#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())

for i in range(n)[::-1]:
    print(" " * i+"*" * (n-i))
    

#input
'''
5
'''
#output
'''
    *
   **
  ***
 ****
*****
'''

