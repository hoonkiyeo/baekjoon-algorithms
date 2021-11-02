#!/usr/bin/env python
# coding: utf-8

# In[11]:


x = input()
y = input()

step1 = int(x) * int(y[-1])
step2 = int(x) * int(y[-2])
step3 = int(x) * int(y[-3])
result = step1 + (step2 * 10) + (step3 * 100)
print(step1)
print(step2)
print(step3)
print(result)


#input
'''
472
385
'''
#output
'''
2360
3776
1416
181720
'''

