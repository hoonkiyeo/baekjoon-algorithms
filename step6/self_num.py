#!/usr/bin/env python
# coding: utf-8

# In[14]:


def self_num(n):
    all_num = set(range(1,n))
    generated_num = set()
    
    for i in range(1,n+1):
        for j in str(i):
            i += int(j)
        if i <= n:
            generated_num.add(i)
    self_num = sorted(all_num - generated_num)
    for num in self_num:
        print(num)
        
self_num(10000)

#output
'''
1
3
5
7
9
20
31
42
53
64
 |
 |       <-- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
'''

