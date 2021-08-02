#!/usr/bin/env python
# coding: utf-8

# In[7]:


#sol_1
def dial_num(dial):
    
    sec = 0
    for letter in dial:
        
        if letter == "A" or letter == "B" or letter == "C":
            sec += 3
        elif letter == "D" or letter == "E" or letter == "F":
            sec += 4
        elif letter == "G" or letter == "H" or letter == "I":
            sec += 5
        elif letter == "J" or letter == "K" or letter == "L":
            sec += 6
        elif letter == "M" or letter == "N" or letter == "O":
            sec += 7
        elif letter == "P" or letter == "Q" or letter == "R" or letter == "S":
            sec += 8
        elif letter == "T" or letter == "U" or letter == "V":
            sec += 9
        else:
            sec += 10
        
    return sec

dial = input()
result = dial_num(dial)
print(result)


#input
'''
UNUCIC
'''
#output
'''
36
'''


# In[9]:


#sol_2

alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
sec = 0

for unit in alphabet_list:
    for i in unit:
        for x in word:
            if i == x:
                sec += alphabet_list.index(unit) + 3
                
print(sec)

#input
'''
UNUCIC
'''
#output
'''
36
'''

