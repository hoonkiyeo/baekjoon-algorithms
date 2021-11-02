#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = int(input())
y = int(input())

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
else:
    quadrant = "origin"
print(quadrant)

#input
'''
12
5
'''
#output
'''
1
'''
#input2
'''
-1
-5
'''
#output2
'''
3
'''

