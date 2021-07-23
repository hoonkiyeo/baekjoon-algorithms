#!/usr/bin/env python
# coding: utf-8

# In[1]:


A,B = map(int,input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

#input
'''
3 3
'''
#output
'''
==
'''
#input2
'''
2 3 
'''
#output2
'''
<
'''

