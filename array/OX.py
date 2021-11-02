#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())

for _ in range(n):
    st = input()
    st_list = list(st)
    score = 0
    cnt = 1
    for a in st_list:
        if a == "O":
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)
    
#input
'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''
#output
'''
10
9
7
55
30
'''

