#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
n = int(input())

for i in range(1,n+1):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    print("Case #%d: %d + %d = %d" % (i, x, y, x+y))
    
#input
'''
5
1 1
2 3
3 4
9 8
5 2
'''
#output
'''
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
'''

