#!/usr/bin/env python
# coding: utf-8

# In[4]:


#sol_1
a = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabets:
    if alphabet in alphabets:
        if alphabet in a:
            print(a.index(alphabet), end = ' ')
        else:
            print(-1, end = ' ')


#input
'''
hoonkiyeo
'''
#output
'''
-1 -1 -1 -1 7 -1 -1 0 5 -1 4 -1 -1 3 1 -1 -1 -1 -1 -1 -1 -1 -1 -1 6 -1 
'''


# In[9]:


#sol_2 (ascii)

word = input()
alphabets = list(range(97,123)) #a to z

for alphabet in alphabets:
    print(word.find(chr(alphabet)), end = ' ')
    
#input
'''
hoonkiyeo
'''
#output
'''
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
'''

