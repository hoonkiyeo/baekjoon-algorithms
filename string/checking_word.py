#!/usr/bin/env python
# coding: utf-8

# In[12]:


def count_group_word(n):
    cnt = 0
    
    for i in range(n):
        word = input()
        error = 0
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                new_word = word[i+1:]
                if new_word.count(word[i]) != 0:
                    error += 1
                    
        if error == 0:
            cnt += 1
    
    return cnt

n = int(input())
result = count_group_word(n)
print(result)


#input
'''
3
happy
new
year
'''
#output
'''
3
'''

