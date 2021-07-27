#!/usr/bin/env python
# coding: utf-8

# In[9]:


a = input()
b = input()
c = input()

num = str(int(a) * int(b) * int(c))

num_dict = {}

for i in range(10):
    num_dict[i] = 0

for letter in num:
    if int(letter) in num_dict:
        num_dict[int(letter)] += 1
    else:
        continue

for value in num_dict.values():
    print(value)
    
#input
'''
150
266
427
'''
#output
'''
3
1
0
2
0
0
0
2
0
0
'''


# In[11]:


#sol_2

a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c))

for i in range(10):
    print(num.count(str(i)))
    
#input
'''
150
266
427
'''
#output
'''
3
1
0
2
0
0
0
2
0
0
'''

