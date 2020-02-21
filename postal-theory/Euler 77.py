# 
# Project Euler 77 Solution
# Copyright (c) Dreamshire. All rights reserved.
# 
# https://blog.dreamshire.com/project-euler-76-solution/
#

#!/usr/bin/env python
# coding: utf-8

# ### Problem 77

# In[1]:


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]

L, target = 5000, 11
while True:
    ways = [1] + [0]*target
    for p in primes:
        for i in range(p, target+1):
            ways[i] += ways[i-p]
    if ways[target] > L: break    
    target += 1
target


# In[ ]:




