#!/usr/bin/env python
# coding: utf-8

# In[17]:


n = int(input())
score_list = list(map(int, input().split()))

max = score_list[0]
avg = 0

for i in score_list:
    if i > max:
        max = i

for i in range(len(score_list)):
    score_list[i] = score_list[i] / max * 100
    


for score in score_list:
    avg += score
    
print(avg / len(score_list))

#input
'''
3
40 80 60
'''
#output
'''
75.0
'''

