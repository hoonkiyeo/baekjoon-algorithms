#!/usr/bin/env python
# coding: utf-8

# In[22]:


def count_word(st):
    word_list = st.split(' ')
    cnt = 0
    
    for word in word_list:
        if word != '':
            cnt += 1
            
    return cnt


st = input()
result = count_word(st)
print(result)



#input
'''
The Curious Case of Benjamin Button
'''
#output
'''
6
'''

