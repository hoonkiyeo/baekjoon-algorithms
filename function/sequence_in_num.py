#!/usr/bin/env python
# coding: utf-8

# In[24]:


#sol_1
def count_sequence():
    n = int(input()) # 0 < n < 1001
    cnt = 0
    
    for i in range(1, n+1):
        if len(str(i)) == 1 or len(str(i)) == 2:
            cnt += 1
        elif int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            cnt += 1
        else:
            continue
    
    return cnt
print(count_sequence())

#input
'''
110
'''
#output
'''
99
'''


# In[54]:


#sol_2

def count_sequence_num(n):
    cnt = 0
    
    if (n < 100):
        return n
    else:
        for i in range(100, n+1):
            hund = (i//100)
            ten = ((i%100)//10)
            one = ((i%100)%10)
            
            if (ten - one) == (hund - ten):
                cnt += 1
        
        
        return (99+cnt)
    
    
n = int(input())
result = count_sequence_num(n)
print(result)

#input
'''
1000
'''
#output
'''
144
'''

