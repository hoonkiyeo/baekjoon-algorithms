#!/usr/bin/env python
# coding: utf-8

# In[20]:


#sol_1
word = input()
word = word.upper()
alpha_dict = {}
alpha_list = []

for alpha in word:
    if alpha in alpha_dict:
        alpha_dict[alpha] += 1
    else:
        alpha_dict[alpha] = 1

min = 0
for count in alpha_dict.values():
    if count > min:
        min = count
        
for alpha in alpha_dict:
    if alpha_dict[alpha] == min:
        alpha_list.append(alpha)
        
if len(alpha_list) > 1:
    print("?")
else:
    print(alpha_list[0])
    
#input
'''
Mississipi
'''
#output
'''
?
'''

