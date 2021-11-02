#!/usr/bin/env python
# coding: utf-8

# In[22]:


import sys

n = int(input())

for _ in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
    
#input
'''
5
1 1
12 34
5 500
40 60
1000 1000
'''
#output
'''
2
46
505
100
2000
'''

