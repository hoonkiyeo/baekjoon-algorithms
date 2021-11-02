#!/usr/bin/env python
# coding: utf-8

# In[19]:



H,M = map(int,input().split())

minute = 60
hour = 24

M = M - 45
if M < 0:
    minute = minute + M
    H -= 1
    if H < 0:
        H = hour + H
    else:
        H = H
else:
    minute = M


print(H, minute, sep = ' ')

# input
'''
23 40
'''
#output
'''
22 55
'''
#input2
'''
0 30
'''
#output2
'''
23 45
'''

