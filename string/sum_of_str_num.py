#!/usr/bin/env python
# coding: utf-8

# In[4]:


#sol_1
n = int(input())
a = input()
sum = 0

for i in a:
    sum += int(i)

print(sum)

#input
'''
11
10987654321
'''
#output
'''
46
'''


# In[6]:


#sol_2

n = input()
a = input()
total = 0

for i in range(int(n)):
    total += int(a[i])
print(total)

#input
'''
5
54321
'''
#output
'''
15
'''

