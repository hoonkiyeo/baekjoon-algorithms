#!/usr/bin/env python
# coding: utf-8

# In[5]:


#sol_1
n = int(input())
cnt = 0
input_num = n

while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    num = (b*10) + c
    
    cnt += 1
    n = num
    if num == input_num:
        print(cnt)
        break

        
#input
'''
26
'''
#output
'''
4
'''


# In[9]:


#sol_2
n = input()
cnt = 0
input_num = n

while True:
    if len(n) == 1:
        n = "0" + n
        input_num = n
    plus = str(int(n[0]) + int(n[1]))
    num = n[-1] + plus[-1]
    cnt += 1
    n = num
    
    if num == input_num:
        print(cnt)
        break
        
#input
'''
55
'''
#output
'''
3
'''

