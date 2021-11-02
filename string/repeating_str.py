#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())

for i in range(n):
    r,s = input().split()
    word = ''
    for i in s:
        
        word += int(r) * i
        
    print(word)
    
    
#input
'''
2
3 ABC
5 /HTP
'''
#output
'''
AAABBBCCC
/////HHHHHTTTTTPPPPP
'''

