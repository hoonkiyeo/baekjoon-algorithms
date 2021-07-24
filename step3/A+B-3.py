#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input())
sum_list = []
for i in range(n):
    x,y = map(int,input().split())
    sum_list.append(x+y)

for i in sum_list:
    print(i)
    
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
2
5
7
17
7
'''

