#!/usr/bin/env python
# coding: utf-8

# In[1]:


#leap year -> 1
#not leap year -> 0
year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)
    
#input
'''
2000
'''
#output
'''
1
'''
#input2
'''
1999
'''
#output2
'''
0
'''

