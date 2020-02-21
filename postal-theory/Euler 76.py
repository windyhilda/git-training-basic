# 
# Project Euler 76 Solution
# Copyright (c) Dreamshire. All rights reserved.
# 
# https://blog.dreamshire.com/project-euler-76-solution/
#

#!/usr/bin/env python
# coding: utf-8

# ### Problem 76

# In[1]:


target = 100
ns = range(1, target)
ways = [1] + [0]*target

for n in ns:
    for i in range(n, target+1):
        ways[i] += ways[i-n]
ways[100]

